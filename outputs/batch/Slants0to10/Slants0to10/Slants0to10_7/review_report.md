# Play-Annotation-Generator Annotation Review — Slants0to10_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_7`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 150
- **Validation Warnings:** 196
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 133
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_PassBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 10 | START | 10 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 13 | START | 106 | 109 |
| ⚠️ START CHANGED | `Action_PassBlock` | RT | `16` | `16` | 13 | START | 103 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 13 | START | 13 | 17 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RG | `19` | `19` | 13 | START | N/A | N/A |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `7` | `7` | 21 | START | 21 | 61 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 21 | END | 10 | 21 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 55 | START | 55 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `7` | `7` | 91 | START | 91 | 185 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 21 | 12 | inferred_complete_timeline |
| `Action_None` | 22 | 54 | 33 | inferred_complete_timeline |
| `Action_ThrowPass` | 55 | 61 | 7 | inferred_complete_timeline |
| `Action_None` | 62 | 75 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 21 | 61 | 41 | inferred_complete_timeline |
| `Action_None` | 62 | 90 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 185 | 95 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–25
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 18 | 9 | inferred_complete_timeline |
| `Action_None` | 23 | 25 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–30
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 30 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 21 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 138 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 142 | 172 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 209 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–11
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 112 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–15
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 15 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–18
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 18 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–27
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 20 | 11 | inferred_complete_timeline |
| `Action_None` | 23 | 27 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 68 | 59 | inferred_complete_timeline |
| `Action_None` | 71 | 210 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 49 | 40 | inferred_complete_timeline |
| `Action_None` | 85 | 87 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 15 | 6 | inferred_complete_timeline |
| `Action_None` | 20 | 25 | 6 | inferred_complete_timeline |
| `Action_None` | 27 | 32 | 6 | inferred_complete_timeline |
| `Action_None` | 35 | 122 | 88 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 18 | 9 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 97 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 105 | 96 | inferred_complete_timeline |
| `Action_None` | 107 | 210 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 189 | 180 | inferred_complete_timeline |
| `Action_None` | 196 | 205 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 9–10 | 2 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 14–130 | 54 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 24–132 | 38 | 8 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 42–210 | 154 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 42–44 | 3 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 44–47 | 4 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 45–210 | 115 | 4 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 58–93 | 19 | 8 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 65–66 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 74–191 | 33 | 6 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 87–210 | 124 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 93–206 | 18 | 5 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 104–210 | 106 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 107–203 | 81 | 8 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 107–210 | 79 | 8 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 113–210 | 93 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 144–210 | 67 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 146–210 | 65 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 146–160 | 9 | 3 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 146–210 | 15 | 2 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 146–151 | 6 | 1 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 146–210 | 51 | 2 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 147–148 | 2 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 159–210 | 52 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 160–210 | 51 | 1 | Undefined position; Undefined team |
| `47` | `64` | Position_Unknown | Team_Unknown | 166–210 | 43 | 2 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 183–187 | 4 | 2 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 189–210 | 22 | 1 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 189–194 | 4 | 2 | Undefined position; Undefined team |
| `51` | `70` | Position_Unknown | Team_Unknown | 200–210 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (4 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `16` (RT): Annotated start 13 != Inferred start 103
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `19` (RG)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 127 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 8: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [10–21], lower_priority='Action_PassBlock' annotated_start=13, effective_Action_PassBlock_start=22.
- ⚠️ Segment 'Action_PassBlock' for track '19' has invalid range: start=13, end=11. Clamping end to start.
- ⚠️ Action 'Action_None' range [10-15] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-25] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-32] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-122] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-18] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '2' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-49] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-18] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-68] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-185] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [191-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-18] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-25] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-189] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-205] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-97] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-15] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-105] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [10-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-138] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [142-172] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-209] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-17] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-21] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 10, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [10-10] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-130] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-33] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-125] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-52] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-69] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-71] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-84] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-143] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-112] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-133] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-188] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-200] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-127] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-138] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-194] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-150] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '39' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-153] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '51' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>