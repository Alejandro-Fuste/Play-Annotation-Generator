# Play-Annotation-Generator Annotation Review — Counter_120

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_120`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 138
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `4` | `3` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `9` | `Group` | 0 | START | 0 | 4 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `13` | `12` | 10 | START | 10 | 15 |
| ✅ EXACT | `Action_DownBlock` | LT | `10` | `9` | 13 | START | 13 | 13 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `6` | `5` | 13 | START | 13 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `15` | `14` | 13 | START | 16 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `11` | `10` | 13 | START | 13 | 40 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 23 | END | 10 | 23 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `4` | `3` | 37 | START | 44 | 48 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `6` | `5` | 49 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 68 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–143
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 23 | 14 | inferred_complete_timeline |
| `Action_None` | 24 | 27 | 4 | inferred_complete_timeline |
| `Action_None` | 32 | 34 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 44 | 48 | 5 | inferred_complete_timeline |
| `Action_None` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_None` | 56 | 70 | 15 | inferred_complete_timeline |
| `Action_None` | 73 | 143 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 13 | 31 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 13 | 40 | 28 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 51 | 52 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 13 | 13 | 1 | inferred_complete_timeline |
| `Action_None` | 15 | 41 | 27 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_None` | 59 | 78 | 20 | inferred_complete_timeline |
| `Action_None` | 83 | 121 | 39 | inferred_complete_timeline |
| `Action_None` | 124 | 130 | 7 | inferred_complete_timeline |
| `Action_None` | 134 | 141 | 8 | inferred_complete_timeline |
| `Action_None` | 144 | 177 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 23 | 14 | inferred_complete_timeline |
| `Action_None` | 39 | 44 | 6 | inferred_complete_timeline |
| `Action_None` | 56 | 77 | 22 | inferred_complete_timeline |
| `Action_None` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_None` | 86 | 91 | 6 | inferred_complete_timeline |
| `Action_None` | 95 | 201 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 15 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 23 | 7 | inferred_complete_timeline |
| `Action_None` | 24 | 40 | 17 | inferred_complete_timeline |
| `Action_None` | 63 | 83 | 21 | inferred_complete_timeline |
| `Action_None` | 99 | 148 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 31 | 22 | inferred_complete_timeline |
| `Action_None` | 98 | 162 | 65 | inferred_complete_timeline |
| `Action_None` | 166 | 239 | 74 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 27 | 18 | inferred_complete_timeline |
| `Action_None` | 30 | 54 | 25 | inferred_complete_timeline |
| `Action_None` | 60 | 62 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 74 | 65 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 48 | 39 | inferred_complete_timeline |
| `Action_None` | 50 | 58 | 9 | inferred_complete_timeline |
| `Action_None` | 61 | 67 | 7 | inferred_complete_timeline |
| `Action_None` | 70 | 99 | 30 | inferred_complete_timeline |
| `Action_None` | 120 | 134 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 53 | 44 | inferred_complete_timeline |
| `Action_None` | 56 | 63 | 8 | inferred_complete_timeline |
| `Action_None` | 67 | 70 | 4 | inferred_complete_timeline |
| `Action_None` | 74 | 88 | 15 | inferred_complete_timeline |
| `Action_None` | 100 | 239 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 63 | 54 | inferred_complete_timeline |
| `Action_None` | 65 | 77 | 13 | inferred_complete_timeline |
| `Action_None` | 81 | 93 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 8–67 | 44 | 7 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 16–43 | 24 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 17–103 | 81 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 43–108 | 62 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 44–191 | 132 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 50–51 | 2 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 65–239 | 175 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 66–92 | 27 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 79–155 | 68 | 4 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 80–172 | 65 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 88–90 | 3 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 102–190 | 88 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 104–107 | 4 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 105–239 | 45 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 108–239 | 132 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 115–174 | 60 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 137–149 | 13 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 158–239 | 82 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 160–163 | 4 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 221–230 | 10 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `4` (QB): Annotated start 37 != Inferred start 44
- ❌ Missing segment for action `Action_BallCarry` on target `6` (RB)

### Track Identity Issues

- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 88 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '5' has invalid range: start=49, end=31. Clamping end to start.
- ⚠️ Action 'Action_None' range [10-63] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-77] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-93] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-27] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-54] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-53] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-63] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-70] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-88] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-27] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-34] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-143] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-48] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-58] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-67] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [13-31] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-23] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-77] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-201] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-74] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '9' starts at frame 13, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [13-13] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-41] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-130] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [13-40] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [51-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-31] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-162] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [10-15] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-26] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [16-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [20-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [23-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [35-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-62] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-62] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-108] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-186] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-92] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-105] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-130] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-131] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-239] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-174] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-149] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-230] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>