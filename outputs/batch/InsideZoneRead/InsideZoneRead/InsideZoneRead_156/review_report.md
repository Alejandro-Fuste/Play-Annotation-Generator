# Play-Annotation-Generator Annotation Review — InsideZoneRead_156

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_156`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 10 | START | 10 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 10 | START | 10 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 10 | START | 10 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 10 | START | 10 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 10 | START | 10 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 10 | START | 10 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 10 | START | 10 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 10 | START | 10 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 10 | START | 10 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 10 | START | 10 | 104 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 105 | START | 105 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `12` | 108 | START | 108 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `15` | 108 | START | 121 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 108 | START | 108 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 108 | START | 108 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 108 | START | 108 | 108 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 120 | END | 105 | 120 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `21` | `20` | 144 | START | 144 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `15` | `14` | 150 | START | 150 | 214 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 200 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_SnapReceive` | 105 | 120 | 16 | inferred_complete_timeline |
| `Action_None` | 121 | 149 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 150 | 214 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 216 | 235 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 240 | 269 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 269 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 229 | 125 | inferred_complete_timeline |
| `Action_None` | 232 | 248 | 17 | inferred_complete_timeline |
| `Action_None` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 269 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 10–154
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 148 | 44 | inferred_complete_timeline |
| `Action_None` | 150 | 154 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 107 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 200 | 93 | inferred_complete_timeline |
| `Action_None` | 201 | 244 | 44 | inferred_complete_timeline |
| `Action_None` | 246 | 269 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 107 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 143 | 36 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 144 | 200 | 57 | inferred_complete_timeline |
| `Action_None` | 201 | 245 | 45 | inferred_complete_timeline |
| `Action_None` | 248 | 269 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 10–127
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_BallSnap` | 105 | 120 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 127 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 10–141
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 53 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 107 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 108 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 119 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 141 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 107 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 143 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 200 | 56 | inferred_complete_timeline |
| `Action_None` | 201 | 269 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 269 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 269 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 201 | 97 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_None` | 208 | 269 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 172 | 68 | inferred_complete_timeline |
| `Action_None` | 177 | 245 | 69 | inferred_complete_timeline |
| `Action_None` | 253 | 269 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 10–253
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 243 | 139 | inferred_complete_timeline |
| `Action_None` | 246 | 253 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 10–241
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 241 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 269 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 269 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 150 | 46 | inferred_complete_timeline |
| `Action_None` | 154 | 269 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 269 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 104 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 269 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 10–269 | 256 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 49–269 | 193 | 6 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 143–185 | 40 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 153–269 | 116 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 165–169 | 5 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 172–269 | 77 | 5 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 231–233 | 3 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 249–251 | 3 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 93 frames exceeds threshold 90 frames [start=108, end=200].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [105–120], lower_priority='Action_ZoneBlock' annotated_start=108, effective_Action_ZoneBlock_start=121.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 93 frames exceeds threshold 90 frames [start=108, end=200].
- ⚠️ Action 'Action_None' range [105-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-241] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-229] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-248] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-269] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-243] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-214] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [216-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [240-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-245] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-244] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-245] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-53] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '21' starts at frame 108, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [108-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-119] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-141] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-73] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-128] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-252] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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