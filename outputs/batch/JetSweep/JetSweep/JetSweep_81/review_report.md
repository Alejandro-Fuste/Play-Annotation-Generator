# Play-Annotation-Generator Annotation Review — JetSweep_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_81`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 9
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE2 | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `18` | `17` | 33 | START | 33 | 59 |
| ✅ EXACT | `Action_BallSnap` | C | `3` | `2` | 34 | START | 34 | 45 |
| ✅ EXACT | `Action_LeadBlock` | RB | `5` | `4` | 39 | START | 39 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE2 | `1` | `0` | 39 | START | 39 | 157 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `13` | 39 | START | 39 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `1` | 39 | START | 39 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `3` | `2` | 39 | START | 46 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `3` | 39 | START | 39 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 39 | START | 39 | 109 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 45 | END | 34 | 45 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 53 | START | 53 | 59 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `14` | `13` | 59 | START | 59 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `17` | 60 | START | 60 | 224 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 109 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 45 | 12 | inferred_complete_timeline |
| `Action_None` | 46 | 52 | 7 | inferred_complete_timeline |
| `Action_Toss` | 53 | 59 | 7 | inferred_complete_timeline |
| `Action_None` | 60 | 132 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_LeadBlock` | 39 | 109 | 71 | inferred_complete_timeline |
| `Action_None` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 239 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_SealBlock` | 39 | 157 | 119 | inferred_complete_timeline |
| `Action_SealBlock` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_SealBlock` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 109 | 71 | inferred_complete_timeline |
| `Action_None` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 109 | 71 | inferred_complete_timeline |
| `Action_None` | 110 | 238 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_BallSnap` | 34 | 45 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 109 | 64 | inferred_complete_timeline |
| `Action_None` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 58 | 20 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 59 | 109 | 51 | inferred_complete_timeline |
| `Action_None` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 109 | 71 | inferred_complete_timeline |
| `Action_None` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 51 | 18 | inferred_complete_timeline |
| `Action_None` | 53 | 55 | 3 | inferred_complete_timeline |
| `Action_None` | 67 | 72 | 6 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 121 | 38 | inferred_complete_timeline |
| `Action_None` | 124 | 212 | 89 | inferred_complete_timeline |
| `Action_None` | 219 | 233 | 15 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 170 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 40 | 7 | inferred_complete_timeline |
| `Action_None` | 52 | 54 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 41 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 96 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 130 | 97 | inferred_complete_timeline |
| `Action_None` | 136 | 139 | 4 | inferred_complete_timeline |
| `Action_None` | 142 | 198 | 57 | inferred_complete_timeline |
| `Action_None` | 202 | 226 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 226 | 193 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–23
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 33–239 | 206 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 47–239 | 187 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 48–239 | 189 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 64–173 | 110 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 79–143 | 57 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 82–239 | 57 | 6 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 105–111 | 7 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 116–239 | 124 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 119–179 | 61 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 120–239 | 120 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 131–138 | 8 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 145–226 | 30 | 5 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 151–239 | 89 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 161–221 | 52 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 172–239 | 67 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 190–239 | 50 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 190–239 | 43 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 192–237 | 26 | 5 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 200–222 | 21 | 3 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 234–236 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SealBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [34–45], lower_priority='Action_ZoneBlock' annotated_start=39, effective_Action_ZoneBlock_start=46.
- ⚠️ Action 'Action_SealBlock' range [39-157] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [159-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-226] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-130] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-226] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-212] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-170] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [60-224] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-57] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-143] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-201] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-217] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-205] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-207] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-215] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '37' has 1 frames without a visible bounding box.
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