# Play-Annotation-Generator Annotation Review — CrackToss_30

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_30`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 298
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | LG | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_CrackBlock` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Toss` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | LG | `12` | `11` | 31 | START | 31 | 50 |
| ❌ MISSING SEGMENT | `Action_CrackBlock` | QB | `4` | `3` | 34 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE | `1` | `0` | 34 | START | 34 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `10` | `9` | 34 | START | 34 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 57 | END | 31 | 57 |
| ✅ EXACT | `Action_Toss` | QB | `4` | `3` | 66 | START | 66 | 99 |
| ✅ EXACT | `Action_BallCarry` | RB | `7` | `6` | 100 | START | 100 | 281 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 233 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 57 | 27 | inferred_complete_timeline |
| `Action_None` | 58 | 65 | 8 | inferred_complete_timeline |
| `Action_Toss` | 66 | 99 | 34 | inferred_complete_timeline |
| `Action_None` | 100 | 259 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 281 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 56 | 26 | inferred_complete_timeline |
| `Action_None` | 66 | 70 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 114 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PullBlock` | 34 | 90 | 57 | inferred_complete_timeline |
| `Action_PullBlock` | 92 | 98 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 126 | 140 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PullBlock` | 34 | 150 | 117 | inferred_complete_timeline |
| `Action_PullBlock` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 158 | 172 | 15 | inferred_complete_timeline |
| `Action_PullBlock` | 176 | 178 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 182 | 198 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 50 | 20 | inferred_complete_timeline |
| `Action_BallSnap` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_None` | 58 | 164 | 107 | inferred_complete_timeline |
| `Action_None` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_None` | 186 | 229 | 44 | inferred_complete_timeline |
| `Action_None` | 249 | 280 | 32 | inferred_complete_timeline |
| `Action_None` | 282 | 298 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 54 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 277 | 247 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 42 | 12 | inferred_complete_timeline |
| `Action_None` | 44 | 56 | 13 | inferred_complete_timeline |
| `Action_None` | 76 | 298 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 164 | 134 | inferred_complete_timeline |
| `Action_None` | 180 | 283 | 104 | inferred_complete_timeline |
| `Action_None` | 291 | 292 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_None` | 52 | 56 | 5 | inferred_complete_timeline |
| `Action_None` | 95 | 104 | 10 | inferred_complete_timeline |
| `Action_None` | 112 | 124 | 13 | inferred_complete_timeline |
| `Action_None` | 126 | 281 | 156 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |
| `Action_None` | 290 | 298 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 76 | 46 | inferred_complete_timeline |
| `Action_None` | 82 | 118 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 136 | 106 | inferred_complete_timeline |
| `Action_None` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 164 | 7 | inferred_complete_timeline |
| `Action_None` | 168 | 182 | 15 | inferred_complete_timeline |
| `Action_None` | 184 | 192 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 116 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 208 | 178 | inferred_complete_timeline |
| `Action_None` | 224 | 287 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 146 | 116 | inferred_complete_timeline |
| `Action_None` | 150 | 174 | 25 | inferred_complete_timeline |
| `Action_None` | 180 | 298 | 119 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–92 | 93 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 41–298 | 250 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 44–96 | 49 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 85–180 | 96 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 125–148 | 24 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 133–298 | 146 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 149–298 | 147 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 152–298 | 135 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 171–298 | 118 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 203–298 | 93 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 221–267 | 36 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 282–298 | 17 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 288–295 | 5 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 288–298 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `12` (2 segments found)
- ❌ Missing segment for action `Action_CrackBlock` on target `4` (QB)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (6 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '0' (TE) duration 107 frames exceeds threshold 90 frames [start=34, end=140].
- ⚠️ Segment 'Action_CrackBlock' for track '3' has invalid range: start=34, end=30. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '9' (LT) duration 177 frames exceeds threshold 90 frames [start=34, end=210].
- ⚠️ Action 'Action_PullBlock' range [34-90] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [92-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [126-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-114] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-76] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-118] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-259] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-287] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-56] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-281] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-298] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [34-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [154-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [158-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [176-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [182-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [204-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-283] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [31-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-280] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-298] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-124] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-281] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-277] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-298] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-54] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-56] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-144] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-253] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-247] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-267] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>