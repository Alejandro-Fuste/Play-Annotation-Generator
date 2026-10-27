# Play-Annotation-Generator Annotation Review — Counter_87

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_87`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 61
- **Validation Warnings:** 43
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 36
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_BallCarry` | TE | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 4 | START | 4 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 4 | START | 4 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 4 | START | 4 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 4 | START | 4 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 4 | START | 4 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 4 | START | 4 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 4 | START | 4 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 4 | START | 4 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 4 | START | 4 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 4 | START | 4 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 4 | START | 4 | 64 |
| ✅ EXACT | `Action_BallSnap` | RG | `21` | `20` | 63 | START | 63 | 64 |
| ✅ EXACT | `Action_DownBlock` | RG | `21` | `20` | 65 | START | 65 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `3` | `2` | 65 | START | 65 | 93 |
| ✅ EXACT | `Action_DownBlock` | LG | `9` | `8` | 65 | START | 65 | 109 |
| ✅ EXACT | `Action_PullBlock` | RT | `20` | `19` | 65 | START | 65 | 159 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `8` | `7` | 65 | START | 65 | 110 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `18` | `17` | 71 | START | 71 | 180 |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 80 | END | 63 | 80 |
| ✅ EXACT | `Action_Handoff` | QB | `22` | `21` | 89 | START | 89 | 110 |
| ✅ EXACT | `Action_BallCarry` | TE | `8` | `7` | 111 | START | 111 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 159 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_SnapReceive` | 63 | 80 | 18 | inferred_complete_timeline |
| `Action_None` | 81 | 88 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 89 | 110 | 22 | inferred_complete_timeline |
| `Action_None` | 111 | 180 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 70 | 67 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 71 | 180 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 64 | 61 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 65 | 110 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 111 | 180 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 4–109
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 64 | 61 | inferred_complete_timeline |
| `Action_DownBlock` | 65 | 109 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 64 | 61 | inferred_complete_timeline |
| `Action_DownBlock` | 65 | 93 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 111 | 159 | 49 | inferred_complete_timeline |
| `Action_None` | 160 | 180 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_BallSnap` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 65 | 159 | 95 | inferred_complete_timeline |
| `Action_None` | 160 | 180 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 64 | 61 | inferred_complete_timeline |
| `Action_PullBlock` | 65 | 159 | 95 | inferred_complete_timeline |
| `Action_None` | 160 | 180 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 123 | 61 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 180 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–135
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 135 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 141 | 79 | inferred_complete_timeline |
| `Action_None` | 144 | 180 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 62 | 59 | inferred_complete_timeline |
| `Action_None` | 63 | 180 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 101–180 | 80 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 162–180 | 11 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 174–178 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 3 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 3 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 6 |
| Missing visible bounding boxes during action | 33 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '2' (C) duration 95 frames exceeds threshold 90 frames [start=65, end=159].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '19' (RT) duration 95 frames exceeds threshold 90 frames [start=65, end=159].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 95 frames exceeds threshold 90 frames [start=65, end=159].
- ⚠️ Action 'Action_None' range [63-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [65-93] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [111-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [111-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [65-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-135] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [71-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [65-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>