# Play-Annotation-Generator Annotation Review — Counter_318

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_318`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 132
- **Validation Warnings:** 162
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 110
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 15 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `17` | `16` | 13 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `14` | `13` | 16 | START | 16 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `17` | `16` | 16 | START | 21 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `5` | `4` | 16 | START | 16 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `3` | `2` | 16 | START | 16 | 31 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `7` | `6` | 16 | START | 16 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `16` | `15` | 24 | END | 13 | 15 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `15` | 39 | START | 39 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `9` | 65 | START | 65 | 73 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 116 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 13 | 15 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 24 | 8 | inferred_complete_timeline |
| `Action_None` | 25 | 38 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 39 | 64 | 26 | inferred_complete_timeline |
| `Action_None` | 65 | 86 | 22 | inferred_complete_timeline |
| `Action_None` | 100 | 115 | 16 | inferred_complete_timeline |
| `Action_None` | 117 | 135 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 65 | 73 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 80 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 47 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 59 | 47 | inferred_complete_timeline |
| `Action_None` | 61 | 104 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 16 | 36 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 48 | 91 | 44 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 113 | 20 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 16 | 32 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 36 | 48 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 55 | 60 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 82 | 112 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 117 | 1 | inferred_complete_timeline |
| `Action_None` | 119 | 144 | 26 | inferred_complete_timeline |
| `Action_None` | 164 | 167 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PullBlock` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_PullBlock` | 71 | 80 | 10 | inferred_complete_timeline |
| `Action_PullBlock` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 103 | 111 | 9 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 16 | 59 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 20 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 115 | 103 | inferred_complete_timeline |
| `Action_None` | 119 | 160 | 42 | inferred_complete_timeline |
| `Action_None` | 169 | 175 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 15 | 3 | inferred_complete_timeline |
| `Action_None` | 18 | 84 | 67 | inferred_complete_timeline |
| `Action_None` | 93 | 139 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 56 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 33 | 21 | inferred_complete_timeline |
| `Action_None` | 35 | 44 | 10 | inferred_complete_timeline |
| `Action_None` | 47 | 68 | 22 | inferred_complete_timeline |
| `Action_None` | 75 | 96 | 22 | inferred_complete_timeline |
| `Action_None` | 98 | 115 | 18 | inferred_complete_timeline |
| `Action_None` | 117 | 157 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 50 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 110 | 98 | inferred_complete_timeline |
| `Action_None` | 117 | 212 | 96 | inferred_complete_timeline |
| `Action_None` | 215 | 221 | 7 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 299 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 104 | 92 | inferred_complete_timeline |
| `Action_None` | 109 | 246 | 138 | inferred_complete_timeline |
| `Action_None` | 252 | 297 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 21–103 | 57 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 24–36 | 10 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 30–121 | 82 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 37–66 | 21 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 45–157 | 61 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 48–128 | 73 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 51–149 | 27 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 56–75 | 18 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 64–101 | 28 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 69–133 | 65 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 76–79 | 4 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 83–86 | 4 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 95–180 | 59 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 113–115 | 3 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 114–180 | 33 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 116–299 | 174 | 4 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 116–299 | 182 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 122–299 | 174 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 145–160 | 12 | 2 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 148–149 | 2 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 163–171 | 9 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 170–262 | 87 | 3 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 225–228 | 4 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 269–288 | 19 | 2 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 284–299 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `17` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (6 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 108 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (RG) duration 101 frames exceeds threshold 90 frames [start=16, end=116].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (LT) duration 101 frames exceeds threshold 90 frames [start=16, end=116].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (LG) duration 101 frames exceeds threshold 90 frames [start=16, end=116].
- ⚠️ Action 'Action_None' range [13-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-104] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-115] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-160] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [16-31] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [71-80] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [82-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [96-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [100-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [103-111] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-47] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [16-36] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [48-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [94-113] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-50] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [16-59] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-56] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-212] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-221] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [65-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [79-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-15] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-139] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-246] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-297] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-33] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-44] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-115] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-157] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [16-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [36-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [55-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [82-112] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 117, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [117-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-20] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [13-15] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-115] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [21-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [31-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [48-58] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-31] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-38] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-52] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-91] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-68] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-158] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-144] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-253] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-277] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-258] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-128] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-171] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-193] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-204] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-262] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-282] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '39' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>