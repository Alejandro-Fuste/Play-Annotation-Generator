# Play-Annotation-Generator Annotation Review — Counter_277

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_277`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `19` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `13` | `12` | 17 | START | 17 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `15` | `14` | 20 | START | 20 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `5` | `4` | 20 | START | 20 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `18` | `17` | 20 | START | 20 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | C | `13` | `12` | 20 | START | 44 | 71 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 31 | END | 17 | 31 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `19` | 47 | START | 47 | 67 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `21` | `20` | 68 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 114 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 31 | 15 | inferred_complete_timeline |
| `Action_None` | 32 | 46 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 47 | 67 | 21 | inferred_complete_timeline |
| `Action_None` | 68 | 180 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 42 | 26 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 20 | 95 | 76 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 114 | 15 | inferred_complete_timeline |
| `Action_None` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_None` | 122 | 124 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 137 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 20 | 95 | 76 | inferred_complete_timeline |
| `Action_DownBlock` | 101 | 110 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 124 | 4 | inferred_complete_timeline |
| `Action_None` | 129 | 145 | 17 | inferred_complete_timeline |
| `Action_None` | 149 | 157 | 9 | inferred_complete_timeline |
| `Action_None` | 163 | 172 | 10 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 28 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 44 | 71 | 28 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 73 | 95 | 23 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 97 | 106 | 10 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 114 | 114 | 1 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 150 | 21 | inferred_complete_timeline |
| `Action_None` | 164 | 173 | 10 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 46 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PullBlock` | 20 | 93 | 74 | inferred_complete_timeline |
| `Action_PullBlock` | 104 | 106 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 48 | 32 | inferred_complete_timeline |
| `Action_None` | 51 | 77 | 27 | inferred_complete_timeline |
| `Action_None` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_None` | 99 | 116 | 18 | inferred_complete_timeline |
| `Action_None` | 131 | 147 | 17 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |
| `Action_None` | 161 | 177 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 79 | 63 | inferred_complete_timeline |
| `Action_None` | 81 | 94 | 14 | inferred_complete_timeline |
| `Action_None` | 104 | 150 | 47 | inferred_complete_timeline |
| `Action_None` | 153 | 157 | 5 | inferred_complete_timeline |
| `Action_None` | 162 | 166 | 5 | inferred_complete_timeline |
| `Action_None` | 168 | 170 | 3 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 120 | 104 | inferred_complete_timeline |
| `Action_None` | 122 | 124 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 137 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 108 | 92 | inferred_complete_timeline |
| `Action_None` | 110 | 141 | 32 | inferred_complete_timeline |
| `Action_None` | 153 | 166 | 14 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 177 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 91 | 75 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 73 | 57 | inferred_complete_timeline |
| `Action_None` | 76 | 180 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 54 | 38 | inferred_complete_timeline |
| `Action_None` | 57 | 61 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 141 | 125 | inferred_complete_timeline |
| `Action_None` | 144 | 180 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–76 | 77 | 2 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–173 | 174 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–105 | 102 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 49–149 | 66 | 5 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 73–180 | 88 | 7 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 105–180 | 76 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 116–120 | 5 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 123–124 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 125–180 | 56 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 130–180 | 51 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 151–180 | 30 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 155–180 | 24 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 164–177 | 9 | 3 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 164–166 | 3 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `13` (5 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `21` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 556: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 556: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ Row 556: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (LT) duration 95 frames exceeds threshold 90 frames [start=20, end=114].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [17–31], lower_priority='Action_PullLeadBlock' annotated_start=20, effective_Action_PullLeadBlock_start=32.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '14' (LG) duration 95 frames exceeds threshold 90 frames [start=20, end=114].
- ⚠️ Segment 'Action_BallCarry' for track '20' has invalid range: start=68, end=37. Clamping end to start.
- ⚠️ Action 'Action_None' range [17-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-141] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [20-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-166] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-120] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-137] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-54] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-42] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-173] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [17-28] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [30-31] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [44-71] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [73-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [97-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [109-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-73] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [20-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [101-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-145] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-172] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-94] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-150] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [20-93] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [104-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-105] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-46] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-53] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-78] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-94] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-126] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-180] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-180] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '31' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>