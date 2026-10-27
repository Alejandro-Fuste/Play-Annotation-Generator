# Play-Annotation-Generator Annotation Review — Counter_99

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_99`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 12 | START | 12 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 12 | START | 12 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 12 | START | 12 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 12 | START | 12 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 12 | START | 12 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 12 | START | 12 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 12 | START | 12 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 12 | START | 12 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 12 | START | 12 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 12 | START | 12 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 12 | START | 12 | 38 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 39 | START | 39 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `14` | `13` | 43 | START | 43 | 67 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `20` | `19` | 43 | START | N/A | N/A |
| ✅ EXACT | `Action_DownBlock` | LT | `4` | `3` | 43 | START | 43 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `21` | `20` | 43 | START | 43 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `15` | `14` | 43 | START | 43 | 98 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | `20` | `19` | 53 | END | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | C | `20` | `19` | 66 | START | 76 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 90 | START | 90 | 98 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 129 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 183 | 145 | inferred_complete_timeline |
| `Action_None` | 185 | 210 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 12–138
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 75 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 89 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 98 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 108 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 137 | 138 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 177 | 139 | inferred_complete_timeline |
| `Action_None` | 180 | 183 | 4 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 210 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 210 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 210 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 12–126
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 42 | 31 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 43 | 98 | 56 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 115 | 121 | 7 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 124 | 126 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 42 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 43 | 129 | 87 | inferred_complete_timeline |
| `Action_None` | 130 | 143 | 14 | inferred_complete_timeline |
| `Action_None` | 149 | 154 | 6 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 210 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 42 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 43 | 67 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 70 | 129 | 60 | inferred_complete_timeline |
| `Action_None` | 130 | 210 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 12–84
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 39 | 53 | 15 | inferred_complete_timeline |
| `Action_None` | 54 | 59 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 83 | 84 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 12–204
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 42 | 31 | inferred_complete_timeline |
| `Action_PullBlock` | 43 | 103 | 61 | inferred_complete_timeline |
| `Action_PullBlock` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 113 | 129 | 17 | inferred_complete_timeline |
| `Action_None` | 130 | 204 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 210 | 172 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 150 | 112 | inferred_complete_timeline |
| `Action_None` | 156 | 177 | 22 | inferred_complete_timeline |
| `Action_None` | 179 | 210 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 74 | 36 | inferred_complete_timeline |
| `Action_None` | 78 | 108 | 31 | inferred_complete_timeline |
| `Action_None` | 110 | 115 | 6 | inferred_complete_timeline |
| `Action_None` | 117 | 140 | 24 | inferred_complete_timeline |
| `Action_None` | 144 | 210 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 117 | 79 | inferred_complete_timeline |
| `Action_None` | 121 | 145 | 25 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 210 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 118 | 80 | inferred_complete_timeline |
| `Action_None` | 124 | 177 | 54 | inferred_complete_timeline |
| `Action_None` | 179 | 210 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 12–151
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 136 | 98 | inferred_complete_timeline |
| `Action_None` | 139 | 147 | 9 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 67 | 29 | inferred_complete_timeline |
| `Action_None` | 69 | 147 | 79 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 177 | 10 | inferred_complete_timeline |
| `Action_None` | 179 | 210 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 210 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 79 | 41 | inferred_complete_timeline |
| `Action_None` | 82 | 157 | 76 | inferred_complete_timeline |
| `Action_None` | 164 | 174 | 11 | inferred_complete_timeline |
| `Action_None` | 179 | 210 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 210 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 12–142
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 142 | 104 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 12–210 | 199 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 91–94 | 4 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 129–210 | 77 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 129–210 | 80 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 134–210 | 76 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 173–210 | 37 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 191–210 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `20` (C)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `15` (3 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `20` (C)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 200: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '19' has invalid range: start=43, end=38. Clamping end to start.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [39–53], lower_priority='Action_DownBlock' annotated_start=43, effective_Action_DownBlock_start=54.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [39–53], lower_priority='Action_SnapReceive' annotated_start=39, effective_Action_SnapReceive_start=54.
- ⚠️ Action 'Action_None' range [39-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-177] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-143] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-79] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-174] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-118] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-177] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [137-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-177] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [43-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [70-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [43-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [115-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [124-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-142] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [76-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [83-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [43-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [107-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [110-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-204] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-162] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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