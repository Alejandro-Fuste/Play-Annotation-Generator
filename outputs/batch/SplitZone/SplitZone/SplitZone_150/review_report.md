# Play-Annotation-Generator Annotation Review — SplitZone_150

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_150`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `11` | `Group` | 23 | START | 24 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 23 | START | 24 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 23 | START | 24 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 23 | START | 24 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 23 | START | 28 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 23 | START | 24 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 23 | START | 24 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 23 | START | 24 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 23 | START | 24 | 53 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 88 | START | 88 | 97 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `12` | 91 | START | 98 | 119 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 91 | START | 91 | 179 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `19` | 91 | START | 91 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `3` | 91 | START | 91 | 138 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 91 | START | 91 | 179 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 97 | END | 88 | 97 |
| ✅ EXACT | `Action_SplitBlock` | HB | `11` | `11` | 99 | START | 99 | 179 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `17` | 113 | START | 113 | 120 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `12` | `12` | 120 | START | 120 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 121 | START | 121 | 238 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 179 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 24–216
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_None` | 98 | 112 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 113 | 120 | 8 | inferred_complete_timeline |
| `Action_None` | 121 | 216 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 24–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 120 | 97 | inferred_complete_timeline |
| `Action_BallCarry` | 121 | 238 | 118 | inferred_complete_timeline |
| `Action_BallCarry` | 240 | 278 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 280 | 299 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 24–290
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 98 | 75 | inferred_complete_timeline |
| `Action_SplitBlock` | 99 | 179 | 81 | inferred_complete_timeline |
| `Action_None` | 180 | 290 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 24–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 299 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 24–273
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 53 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 90 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 179 | 89 | inferred_complete_timeline |
| `Action_None` | 180 | 273 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 28–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 38 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 90 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 179 | 89 | inferred_complete_timeline |
| `Action_None` | 180 | 299 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 24–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 119 | 22 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 120 | 179 | 60 | inferred_complete_timeline |
| `Action_None` | 180 | 299 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 24–157
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 90 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 138 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 157 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 24–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 90 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 179 | 89 | inferred_complete_timeline |
| `Action_None` | 180 | 299 | 120 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 24–299
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 111 | 24 | inferred_complete_timeline |
| `Action_None` | 119 | 128 | 10 | inferred_complete_timeline |
| `Action_None` | 131 | 210 | 80 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 232 | 5 | inferred_complete_timeline |
| `Action_None` | 238 | 299 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 24–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 152 | 65 | inferred_complete_timeline |
| `Action_None` | 154 | 299 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 24–223
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 128 | 41 | inferred_complete_timeline |
| `Action_None` | 130 | 142 | 13 | inferred_complete_timeline |
| `Action_None` | 147 | 167 | 21 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 24–222
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 160 | 73 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 24–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 131 | 44 | inferred_complete_timeline |
| `Action_None` | 137 | 299 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 24–266
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 266 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 24–266
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 266 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 24–141
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 141 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 24–290
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 290 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 24–222
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 88 | 219 | 132 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 24–104 | 81 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 37–39 | 3 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 56–59 | 4 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 119–212 | 32 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 130–242 | 92 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 152–299 | 148 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 165–263 | 99 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 202–299 | 76 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 215–269 | 5 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 234–299 | 66 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 247–299 | 53 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 290–299 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 91 != Inferred start 98
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [88–97], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=98.
- ⚠️ Action 'Action_None' range [88-131] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-157] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-238] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [240-278] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [280-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-53] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-273] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-290] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-266] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-219] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-290] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-38] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-44] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-39] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-212] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-242] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-263] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-273] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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