# Play-Annotation-Generator Annotation Review — Counter_100

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_100`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `14` | `13` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 78 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 74 | START | 74 | 88 |
| ✅ EXACT | `Action_DownBlock` | LT | `1` | `0` | 79 | START | 79 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `5` | `4` | 79 | START | 90 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `6` | `5` | 79 | START | 79 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `14` | `13` | 79 | START | 79 | 90 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `3` | `2` | 79 | START | 79 | 162 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 88 | END | 74 | 88 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `3` | 100 | START | 100 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `7` | `6` | 124 | START | 124 | 125 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 162 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 88 | 15 | inferred_complete_timeline |
| `Action_None` | 89 | 99 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 100 | 123 | 24 | inferred_complete_timeline |
| `Action_None` | 124 | 204 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 99–239
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 99 | 104 | 6 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 79 | 162 | 84 | inferred_complete_timeline |
| `Action_None` | 163 | 239 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 162 | 84 | inferred_complete_timeline |
| `Action_None` | 163 | 239 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 96 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 109 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 162 | 51 | inferred_complete_timeline |
| `Action_None` | 163 | 239 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 88 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 90 | 162 | 73 | inferred_complete_timeline |
| `Action_None` | 163 | 203 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PullBlock` | 79 | 90 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 92 | 101 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 104 | 132 | 29 | inferred_complete_timeline |
| `Action_PullBlock` | 138 | 162 | 25 | inferred_complete_timeline |
| `Action_None` | 163 | 212 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 98 | 25 | inferred_complete_timeline |
| `Action_None` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_None` | 148 | 209 | 62 | inferred_complete_timeline |
| `Action_None` | 216 | 239 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 143 | 70 | inferred_complete_timeline |
| `Action_None` | 151 | 239 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 121 | 48 | inferred_complete_timeline |
| `Action_None` | 128 | 148 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 92 | 19 | inferred_complete_timeline |
| `Action_None` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_None` | 112 | 121 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 122–239
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 122 | 230 | 109 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 198 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 160 | 87 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–15
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 163 | 90 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–225 | 222 | 4 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–236 | 206 | 7 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 124–239 | 114 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 137–193 | 57 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 157–224 | 68 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 171–239 | 69 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 189–208 | 20 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 191–239 | 48 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 216–239 | 23 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [74–88], lower_priority='Action_DownBlock' annotated_start=79, effective_Action_DownBlock_start=89.
- ⚠️ Action 'Action_DownBlock' range [79-162] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [79-162] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [74-88] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [100-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [124-125] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-225] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-143] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-160] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-239] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-148] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-206] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-236] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [79-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [92-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [104-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-209] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-230] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-208] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>