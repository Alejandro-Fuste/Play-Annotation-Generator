# Play-Annotation-Generator Annotation Review — Counter_313

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_313`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 1
- **Action Segments:** 86
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 72 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 27 | START | 27 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `16` | 30 | START | 43 | 121 |
| ✅ EXACT | `Action_DownBlock` | LG | `18` | `17` | 30 | START | 30 | 106 |
| ✅ EXACT | `Action_DownBlock` | LT | `22` | `21` | 30 | START | 30 | 94 |
| ✅ EXACT | `Action_PullBlock` | RG | `20` | `19` | 30 | START | 30 | 121 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `15` | `14` | 30 | START | 30 | 121 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `20` | 42 | END | 27 | 42 |
| ✅ EXACT | `Action_Handoff` | QB | `21` | `20` | 55 | START | 55 | 72 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `5` | 73 | START | 73 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 121 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 42 | 16 | inferred_complete_timeline |
| `Action_None` | 43 | 54 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 55 | 72 | 18 | inferred_complete_timeline |
| `Action_None` | 73 | 180 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_BallCarry` | 73 | 180 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 180 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 180 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 57 | 31 | inferred_complete_timeline |
| `Action_None` | 60 | 94 | 35 | inferred_complete_timeline |
| `Action_None` | 103 | 180 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 129 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 30 | 94 | 65 | inferred_complete_timeline |
| `Action_None` | 160 | 168 | 9 | inferred_complete_timeline |
| `Action_None` | 172 | 180 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 30 | 106 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 42 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 43 | 121 | 79 | inferred_complete_timeline |
| `Action_None` | 122 | 180 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PullBlock` | 30 | 121 | 92 | inferred_complete_timeline |
| `Action_None` | 122 | 180 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 30 | 121 | 92 | inferred_complete_timeline |
| `Action_None` | 122 | 180 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 58 | 32 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 180 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 52 | 26 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 98 | 9 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 88 | 62 | inferred_complete_timeline |
| `Action_None` | 106 | 122 | 17 | inferred_complete_timeline |
| `Action_None` | 126 | 180 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 78 | 52 | inferred_complete_timeline |
| `Action_None` | 80 | 101 | 22 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 118 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 160 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 146 | 120 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 180 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 109 | 83 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 156 | 37 | inferred_complete_timeline |
| `Action_None` | 158 | 180 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 170 | 144 | inferred_complete_timeline |
| `Action_None` | 174 | 180 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–110 | 101 | 3 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–84 | 82 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 76–180 | 98 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 79–84 | 6 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 104–180 | 77 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 109–180 | 70 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 112–180 | 63 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 124–180 | 57 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 163–180 | 18 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 163–178 | 16 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 168–179 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | 72 | 72 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '24' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '16' (C) duration 92 frames exceeds threshold 90 frames [start=30, end=121].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [27–42], lower_priority='Action_DownBlock' annotated_start=30, effective_Action_DownBlock_start=43.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '19' (RG) duration 92 frames exceeds threshold 90 frames [start=30, end=121].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (LT) duration 92 frames exceeds threshold 90 frames [start=30, end=121].
- ⚠️ Action 'Action_None' range [27-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-80] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-75] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-88] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-122] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-180] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [73-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-160] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-129] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-170] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [30-121] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [43-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [30-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-52] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-98] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [30-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [30-94] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-156] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-136] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-180] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-178] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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