# Play-Annotation-Generator Annotation Review — SplitZone_124

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_124`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 43 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 44 | START | 44 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `10` | `10` | 46 | START | 46 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `12` | 47 | START | 47 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `13` | 47 | START | 47 | 58 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `5` | 47 | START | 47 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `8` | 47 | START | 47 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `9` | 47 | START | 57 | 71 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 56 | END | 44 | 56 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `6` | 64 | START | 64 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `7` | 71 | START | 71 | 77 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 122 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 56 | 13 | inferred_complete_timeline |
| `Action_None` | 57 | 63 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 64 | 70 | 7 | inferred_complete_timeline |
| `Action_None` | 71 | 79 | 9 | inferred_complete_timeline |
| `Action_None` | 81 | 193 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 77 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 219 | 141 | inferred_complete_timeline |
| `Action_BallCarry` | 229 | 269 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SplitBlock` | 46 | 74 | 29 | inferred_complete_timeline |
| `Action_SplitBlock` | 81 | 122 | 42 | inferred_complete_timeline |
| `Action_None` | 123 | 212 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 94 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 122 | 1 | inferred_complete_timeline |
| `Action_None` | 123 | 269 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 122 | 76 | inferred_complete_timeline |
| `Action_None` | 123 | 269 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_BallSnap` | 44 | 56 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 71 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 107 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 122 | 5 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 121 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 58 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 102 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 108 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 231 | 188 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |
| `Action_None` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 93 | 50 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 120 | 13 | inferred_complete_timeline |
| `Action_None` | 122 | 140 | 19 | inferred_complete_timeline |
| `Action_None` | 142 | 225 | 84 | inferred_complete_timeline |
| `Action_None` | 234 | 236 | 3 | inferred_complete_timeline |
| `Action_None` | 239 | 269 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 71 | 28 | inferred_complete_timeline |
| `Action_None` | 73 | 115 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 97 | 54 | inferred_complete_timeline |
| `Action_None` | 105 | 118 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 130 | 87 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 181 | 38 | inferred_complete_timeline |
| `Action_None` | 184 | 214 | 31 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 122 | 79 | inferred_complete_timeline |
| `Action_None` | 126 | 196 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 115 | 72 | inferred_complete_timeline |
| `Action_None` | 118 | 219 | 102 | inferred_complete_timeline |
| `Action_None` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 68–108 | 38 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 68–230 | 115 | 7 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 115–216 | 71 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 119–122 | 4 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 119–222 | 72 | 10 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 145–208 | 58 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 147–269 | 115 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 151–223 | 73 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 153–269 | 117 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 168–170 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 168–188 | 21 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 182–269 | 88 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 186–192 | 6 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 189–269 | 81 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 201–209 | 9 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 252–269 | 18 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 252–254 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [44–56], lower_priority='Action_ZoneBlock' annotated_start=47, effective_Action_ZoneBlock_start=57.
- ⚠️ Action 'Action_None' range [44-122] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-196] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-181] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-214] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-115] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-115] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-219] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-121] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-77] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [79-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-71] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [46-74] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-93] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-269] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-97] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-155] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-230] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-152] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-150] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-208] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-208] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-246] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-223] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-209] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>