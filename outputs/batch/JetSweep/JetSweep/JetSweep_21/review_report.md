# Play-Annotation-Generator Annotation Review — JetSweep_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_21`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 29
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `7` | `6` |
| ✅ EXACT | `Action_BallSnap` | WR | offense | `7` | `6` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `7` | `6` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT | defense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `17` | `16` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `19` | `18` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `21` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `22` | `21` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `6` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `7` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `8` | `Group` | 0 | START | 0 | 36 |
| ✅ EXACT | `Action_JetMotion` | WR | `7` | `6` | 24 | START | 24 | 36 |
| ✅ EXACT | `Action_BallSnap` | WR | `7` | `6` | 37 | START | 37 | 49 |
| ✅ EXACT | `Action_LeadBlock` | RB | `3` | `2` | 42 | START | 42 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `16` | 42 | START | 42 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `18` | 42 | START | 42 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 42 | START | 42 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `22` | `21` | 42 | START | 42 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 42 | START | 42 | 114 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 49 | END | 37 | 49 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 54 | START | 54 | 64 |
| ✅ EXACT | `Action_BallCarry` | WR | `7` | `6` | 65 | START | 65 | 205 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT | `20` | `19` | 72 | START | 72 | 114 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `17` | `16` | 114 | BOUNDARY | 62 | 114 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `19` | `18` | 114 | BOUNDARY | 107 | 114 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `21` | `20` | 114 | BOUNDARY | 74 | 114 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `22` | `21` | 114 | BOUNDARY | 79 | 114 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `6` | `5` | 114 | BOUNDARY | 42 | 114 |

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
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 49 | 13 | inferred_complete_timeline |
| `Action_None` | 50 | 53 | 4 | inferred_complete_timeline |
| `Action_Toss` | 54 | 64 | 11 | inferred_complete_timeline |
| `Action_None` | 65 | 143 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_LeadBlock` | 42 | 114 | 73 | inferred_complete_timeline |
| `Action_None` | 115 | 123 | 9 | inferred_complete_timeline |
| `Action_None` | 125 | 238 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 237 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 239 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_JetMotion` | 24 | 36 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 49 | 13 | inferred_complete_timeline |
| `Action_None` | 50 | 64 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 65 | 205 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 142 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 114 | 73 | inferred_complete_timeline |
| `Action_None` | 115 | 239 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 62 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 114 | 41 | inferred_complete_timeline |
| `Action_None` | 115 | 239 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 59 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 114 | 53 | inferred_complete_timeline |
| `Action_None` | 115 | 239 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 103 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 114 | 8 | inferred_complete_timeline |
| `Action_None` | 115 | 173 | 59 | inferred_complete_timeline |
| `Action_None` | 175 | 239 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 77 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 114 | 36 | inferred_complete_timeline |
| `Action_None` | 115 | 239 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 69 | 33 | inferred_complete_timeline |
| `Action_None` | 71 | 154 | 84 | inferred_complete_timeline |
| `Action_None` | 158 | 236 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 70 | 34 | inferred_complete_timeline |
| `Action_None` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 89 | 166 | 78 | inferred_complete_timeline |
| `Action_None` | 171 | 173 | 3 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |
| `Action_None` | 181 | 198 | 18 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 227 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 72 | 114 | 43 | inferred_complete_timeline |
| `Action_None` | 115 | 176 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 140 | 104 | inferred_complete_timeline |
| `Action_None` | 142 | 183 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 239 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 148 | 112 | inferred_complete_timeline |
| `Action_None` | 159 | 162 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 238 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 158 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 151 | 115 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_None` | 162 | 170 | 9 | inferred_complete_timeline |
| `Action_None` | 172 | 234 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 239 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 183 | 147 | inferred_complete_timeline |
| `Action_None` | 189 | 195 | 7 | inferred_complete_timeline |
| `Action_None` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_None` | 206 | 228 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 12–38 | 9 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 93–95 | 3 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 135–234 | 100 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 145–150 | 6 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 164–216 | 53 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 169–171 | 3 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 177–233 | 56 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 54 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [37-237] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-123] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-238] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-69] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-236] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-238] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-239] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [65-205] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-142] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-158] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-170] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-148] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-195] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-228] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-77] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-15] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-216] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-189] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '29' has 1 frames without a visible bounding box.
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