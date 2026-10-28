# Play-Annotation-Generator Annotation Review — Draw_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_57`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 43 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 41 | START | 41 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `17` | 44 | START | 44 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `19` | 44 | START | 44 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `20` | 44 | START | 52 | 70 |
| ✅ EXACT | `Action_PassBlock` | RT | `22` | `21` | 44 | START | 44 | 105 |
| ✅ EXACT | `Action_PassBlock` | LT | `7` | `6` | 44 | START | 44 | 105 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 51 | END | 41 | 51 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `14` | `13` | 61 | START | 61 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `14` | `13` | 83 | START | 83 | 179 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 105 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_None` | 52 | 60 | 9 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 61 | 82 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 83 | 179 | 97 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 189 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 89 | 49 | inferred_complete_timeline |
| `Action_None` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 119 | 79 | inferred_complete_timeline |
| `Action_None` | 124 | 199 | 76 | inferred_complete_timeline |
| `Action_None` | 202 | 239 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 105 | 62 | inferred_complete_timeline |
| `Action_None` | 106 | 239 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 59 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 81 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 105 | 20 | inferred_complete_timeline |
| `Action_None` | 106 | 166 | 61 | inferred_complete_timeline |
| `Action_None` | 190 | 239 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_BallSnap` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 70 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 105 | 17 | inferred_complete_timeline |
| `Action_None` | 106 | 239 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 86 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 105 | 1 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 105 | 62 | inferred_complete_timeline |
| `Action_None` | 106 | 239 | 134 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 77 | 37 | inferred_complete_timeline |
| `Action_None` | 116 | 119 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 64 | 24 | inferred_complete_timeline |
| `Action_None` | 69 | 235 | 167 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 182 | 142 | inferred_complete_timeline |
| `Action_None` | 184 | 239 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 76 | 36 | inferred_complete_timeline |
| `Action_None` | 98 | 239 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 184 | 144 | inferred_complete_timeline |
| `Action_None` | 199 | 202 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 162 | 122 | inferred_complete_timeline |
| `Action_None` | 164 | 239 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 140 | 100 | inferred_complete_timeline |
| `Action_None` | 142 | 239 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 201 | 161 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 153 | 113 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 80–110 | 31 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 91–99 | 9 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 105–110 | 5 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 120–239 | 120 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 128–239 | 112 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 191–229 | 19 | 4 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 204–206 | 3 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 204–215 | 12 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 218–220 | 3 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 229–239 | 10 | 2 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 230–231 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [41–51], lower_priority='Action_PassBlock' annotated_start=44, effective_Action_PassBlock_start=52.
- ⚠️ Action 'Action_None' range [41-119] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-199] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-184] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-77] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-162] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-239] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-182] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [83-179] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-235] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-89] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-110] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-99] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-215] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '35' has 1 frames without a visible bounding box.
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

</details>