# Play-Annotation-Generator Annotation Review — JetSweep_170

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_170`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB2 | defense | `11` | `10` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Toss` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 31 |
| ✅ EXACT | `Action_BallSnap` | LB2 | `11` | `10` | 32 | START | 32 | 48 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `18` | `16` | 34 | START | 34 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `13` | `12` | 34 | START | 34 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `13` | 34 | START | 34 | 87 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `15` | `14` | 34 | START | 34 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `5` | `4` | 34 | START | 34 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `6` | 34 | START | 34 | 50 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 48 | END | 32 | 48 |
| ✅ EXACT | `Action_Toss` | QB | `6` | `5` | 55 | START | 55 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `16` | 65 | START | 65 | 158 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 87 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_None` | 49 | 54 | 6 | inferred_complete_timeline |
| `Action_Toss` | 55 | 64 | 10 | inferred_complete_timeline |
| `Action_None` | 65 | 269 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 269 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_LeadBlock` | 34 | 54 | 21 | inferred_complete_timeline |
| `Action_LeadBlock` | 57 | 87 | 31 | inferred_complete_timeline |
| `Action_None` | 88 | 95 | 8 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 108 | 269 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 50 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 66 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 87 | 54 | inferred_complete_timeline |
| `Action_None` | 88 | 269 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 53 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 87 | 32 | inferred_complete_timeline |
| `Action_None` | 88 | 269 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 87 | 54 | inferred_complete_timeline |
| `Action_None` | 88 | 161 | 74 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 81 | 50 | inferred_complete_timeline |
| `Action_None` | 85 | 269 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 269 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 60 | 29 | inferred_complete_timeline |
| `Action_None` | 63 | 72 | 10 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 269 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 269 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_None` | 49 | 269 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 169 | 138 | inferred_complete_timeline |
| `Action_None` | 172 | 258 | 87 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 188 | 157 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_None` | 200 | 213 | 14 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 246 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–269 | 266 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 34–269 | 232 | 5 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 37–41 | 5 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 58–196 | 139 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 59–74 | 16 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 61–88 | 6 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 79–196 | 98 | 3 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 86–113 | 8 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 100–109 | 10 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 110–269 | 160 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 153–169 | 10 | 2 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 162–211 | 50 | 1 | Undefined position; Undefined team |
| `27` | `46` | Position_Unknown | Team_Unknown | 185–238 | 54 | 1 | Undefined position; Undefined team |
| `28` | `48` | Position_Unknown | Team_Unknown | 207–226 | 18 | 3 | Undefined position; Undefined team |
| `29` | `49` | Position_Unknown | Team_Unknown | 209–269 | 61 | 1 | Undefined position; Undefined team |
| `30` | `50` | Position_Unknown | Team_Unknown | 214–269 | 56 | 1 | Undefined position; Undefined team |
| `31` | `51` | Position_Unknown | Team_Unknown | 216–245 | 27 | 2 | Undefined position; Undefined team |
| `32` | `56` | Position_Unknown | Team_Unknown | 257–258 | 2 | 1 | Undefined position; Undefined team |
| `33` | `57` | Position_Unknown | Team_Unknown | 258–269 | 12 | 1 | Undefined position; Undefined team |
| `34` | `59` | Position_Unknown | Team_Unknown | 262–269 | 8 | 1 | Undefined position; Undefined team |
| `35` | `60` | Position_Unknown | Team_Unknown | 262–269 | 8 | 1 | Undefined position; Undefined team |
| `36` | `61` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |
| `37` | `62` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 342: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [32-113] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-269] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-258] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-53] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-50] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-66] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-70] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-188] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-246] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-72] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [34-54] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-269] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [65-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [161-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [164-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [167-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-196] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-113] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-238] for track '27' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-221] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>