# Play-Annotation-Generator Annotation Review — Counter_340

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_340`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 99 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 97 | START | 97 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 100 | START | 112 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `4` | `3` | 100 | START | 100 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `9` | `8` | 100 | START | 100 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `3` | `2` | 100 | START | 100 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `2` | `1` | 100 | START | 100 | 167 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `10` | `9` | 108 | START | 108 | 144 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 111 | END | 97 | 111 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 124 | START | 124 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `9` | 145 | START | 145 | 215 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 209 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_SnapReceive` | 97 | 111 | 15 | inferred_complete_timeline |
| `Action_None` | 112 | 123 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 124 | 144 | 21 | inferred_complete_timeline |
| `Action_None` | 145 | 269 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 108 | 144 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 145 | 215 | 71 | inferred_complete_timeline |
| `Action_BallCarry` | 217 | 269 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 164 | 68 | inferred_complete_timeline |
| `Action_None` | 166 | 207 | 42 | inferred_complete_timeline |
| `Action_None` | 212 | 257 | 46 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 164 | 65 | inferred_complete_timeline |
| `Action_DownBlock` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 172 | 209 | 38 | inferred_complete_timeline |
| `Action_None` | 210 | 269 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 126 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 209 | 82 | inferred_complete_timeline |
| `Action_None` | 210 | 269 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_BallSnap` | 97 | 111 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 156 | 41 | inferred_complete_timeline |
| `Action_DownBlock` | 160 | 209 | 50 | inferred_complete_timeline |
| `Action_None` | 210 | 260 | 51 | inferred_complete_timeline |
| `Action_None` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_PullBlock` | 100 | 119 | 20 | inferred_complete_timeline |
| `Action_PullBlock` | 122 | 209 | 88 | inferred_complete_timeline |
| `Action_None` | 210 | 237 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 100 | 167 | 68 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 181 | 209 | 29 | inferred_complete_timeline |
| `Action_None` | 210 | 269 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 269 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 122 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 123 | 27 | inferred_complete_timeline |
| `Action_None` | 125 | 148 | 24 | inferred_complete_timeline |
| `Action_None` | 150 | 256 | 107 | inferred_complete_timeline |
| `Action_None` | 262 | 267 | 6 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 106 | 10 | inferred_complete_timeline |
| `Action_None` | 155 | 269 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 184 | 88 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 129 | 33 | inferred_complete_timeline |
| `Action_None` | 133 | 144 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `18` | Position_Unknown | Team_Unknown | 137–269 | 102 | 4 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 139–269 | 131 | 1 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 141–267 | 127 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 146–269 | 113 | 3 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 157–269 | 110 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 158–269 | 107 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 168–268 | 98 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 193–269 | 73 | 2 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 198–225 | 28 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 199–269 | 67 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 201–269 | 69 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 241–269 | 29 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 243–248 | 6 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 244–246 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (RG) duration 110 frames exceeds threshold 90 frames [start=100, end=209].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (LT) duration 110 frames exceeds threshold 90 frames [start=100, end=209].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (LG) duration 110 frames exceeds threshold 90 frames [start=100, end=209].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (C) duration 110 frames exceeds threshold 90 frames [start=100, end=209].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [97–111], lower_priority='Action_DownBlock' annotated_start=100, effective_Action_DownBlock_start=112.
- ⚠️ Action 'Action_None' range [97-164] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-207] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-257] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [100-167] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [170-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [175-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [100-119] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [100-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [169-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-148] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-256] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-144] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [100-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [108-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '9' starts at frame 145, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [145-215] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [217-269] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-260] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-269] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-212] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-267] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-228] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-175] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-263] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-240] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-225] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>