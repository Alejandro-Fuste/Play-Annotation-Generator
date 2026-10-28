# Play-Annotation-Generator Annotation Review — Draw_96

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_96`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 131
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | RT | offense | `16` | `15` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 29 | START | 29 | 42 |
| ✅ EXACT | `Action_PassBlock` | LT | `14` | `13` | 32 | START | 32 | 120 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RT | `16` | `15` | 32 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `19` | 32 | START | 32 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `20` | 32 | START | 43 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `22` | `21` | 32 | START | 32 | 50 |
| ✅ EXACT | `Action_SnapReceive` | RT | `16` | `15` | 42 | END | 29 | 42 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | RT | `16` | `15` | 46 | START | 46 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | `16` | `15` | 87 | START | 87 | 127 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 120 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 125 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 114 | 86 | inferred_complete_timeline |
| `Action_None` | 116 | 210 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 181 | 153 | inferred_complete_timeline |
| `Action_None` | 183 | 190 | 8 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 120 | 89 | inferred_complete_timeline |
| `Action_None` | 121 | 210 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 120 | 89 | inferred_complete_timeline |
| `Action_None` | 121 | 151 | 31 | inferred_complete_timeline |
| `Action_None` | 153 | 161 | 9 | inferred_complete_timeline |
| `Action_None` | 167 | 170 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_BallSnap` | 29 | 42 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 109 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 50 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 70 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 120 | 44 | inferred_complete_timeline |
| `Action_None` | 121 | 165 | 45 | inferred_complete_timeline |
| `Action_None` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 210 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 42 | 14 | inferred_complete_timeline |
| `Action_None` | 43 | 45 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 46 | 86 | 41 | inferred_complete_timeline |
| `Action_BallCarry` | 87 | 127 | 41 | inferred_complete_timeline |
| `Action_BallCarry` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 151 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 153 | 160 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 157 | 129 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_None` | 175 | 179 | 5 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 210 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 178 | 150 | inferred_complete_timeline |
| `Action_None` | 181 | 184 | 4 | inferred_complete_timeline |
| `Action_None` | 186 | 210 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 125 | 97 | inferred_complete_timeline |
| `Action_None` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 146 | 118 | inferred_complete_timeline |
| `Action_None` | 148 | 165 | 18 | inferred_complete_timeline |
| `Action_None` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_None` | 175 | 179 | 5 | inferred_complete_timeline |
| `Action_None` | 181 | 210 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 47 | 19 | inferred_complete_timeline |
| `Action_None` | 49 | 111 | 63 | inferred_complete_timeline |
| `Action_None` | 113 | 210 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 135 | 107 | inferred_complete_timeline |
| `Action_None` | 138 | 144 | 7 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 118 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 85 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–178 | 177 | 4 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 68–210 | 133 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 112–131 | 12 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 121–210 | 88 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 126–208 | 77 | 5 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 134–136 | 3 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 140–196 | 47 | 5 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 142–168 | 17 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 149–158 | 10 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 172–178 | 7 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 172–210 | 39 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 173–186 | 13 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 175–177 | 3 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 190–210 | 19 | 2 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 192–210 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_PassBlock` on target `16` (RT)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 87 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 191: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_PassBlock' for track '15' has invalid range: start=32, end=28. Clamping end to start.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [29–42], lower_priority='Action_PassBlock' annotated_start=32, effective_Action_PassBlock_start=43.
- ⚠️ Action 'Action_None' range [29-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-181] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-85] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-67] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-125] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-157] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [87-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [139-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [153-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [167-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-146] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-151] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-109] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-120] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-165] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-204] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-186] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-202] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-168] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-177] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-148] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-186] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>