# Play-Annotation-Generator Annotation Review — JetSweep_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_29`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 59
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 29
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-F | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-Y | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `9` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Toss` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `9` | `8` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `22` | `21` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `15` | `14` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `17` | `16` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `21` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `22` | `21` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `6` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-F | `1` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `10` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-Y | `4` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `9` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_JetMotion` | WR | `9` | `8` | 46 | START | 46 | 102 |
| ✅ EXACT | `Action_BallSnap` | C | `6` | `5` | 74 | START | 74 | 89 |
| ✅ EXACT | `Action_LeadBlock` | RB | `2` | `1` | 78 | START | 78 | 148 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 78 | START | 78 | 148 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `16` | 78 | START | 78 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 78 | START | 78 | 108 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `22` | `21` | 78 | START | 78 | 104 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `6` | `5` | 78 | START | 90 | 148 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 89 | END | 74 | 89 |
| ✅ EXACT | `Action_Toss` | QB | `18` | `17` | 92 | START | 92 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `9` | `8` | 103 | START | 103 | 180 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `22` | `21` | 105 | START | 105 | 148 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `15` | `14` | 148 | BOUNDARY | 78 | 148 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `17` | `16` | 148 | BOUNDARY | 78 | 148 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `21` | `20` | 148 | BOUNDARY | 119 | 148 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `22` | `21` | 148 | BOUNDARY | 105 | 148 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `6` | `5` | 148 | BOUNDARY | 90 | 148 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 89 | 16 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_Toss` | 92 | 102 | 11 | inferred_complete_timeline |
| `Action_None` | 103 | 239 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_LeadBlock` | 78 | 148 | 71 | inferred_complete_timeline |
| `Action_None` | 149 | 158 | 10 | inferred_complete_timeline |
| `Action_None` | 163 | 192 | 30 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 201 | 211 | 11 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_JetMotion` | 46 | 102 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 180 | 78 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 192 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 194 | 206 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 210 | 230 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 239 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>TE-F — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 206 | 133 | inferred_complete_timeline |
| `Action_None` | 208 | 235 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>TE-Y — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 183 | 110 | inferred_complete_timeline |
| `Action_None` | 185 | 192 | 8 | inferred_complete_timeline |
| `Action_None` | 194 | 231 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 148 | 71 | inferred_complete_timeline |
| `Action_None` | 149 | 221 | 73 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 108 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 148 | 30 | inferred_complete_timeline |
| `Action_None` | 149 | 229 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 89 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 148 | 59 | inferred_complete_timeline |
| `Action_None` | 149 | 234 | 86 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 148 | 71 | inferred_complete_timeline |
| `Action_None` | 149 | 239 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 104 | 27 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 105 | 148 | 44 | inferred_complete_timeline |
| `Action_None` | 149 | 239 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 239 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 227 | 154 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 239 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 174 | 101 | inferred_complete_timeline |
| `Action_None` | 178 | 206 | 29 | inferred_complete_timeline |
| `Action_None` | 210 | 239 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 129 | 56 | inferred_complete_timeline |
| `Action_None` | 135 | 210 | 76 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 172 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 239 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 171 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 175 | 102 | inferred_complete_timeline |
| `Action_None` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 229 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 206 | 133 | inferred_complete_timeline |
| `Action_None` | 208 | 216 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 239 | 166 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–106 | 19 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 85–88 | 4 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 186–227 | 42 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 190–239 | 50 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 203–212 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `6` (C): Annotated start 78 != Inferred start 90
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [74–89], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=90.
- ⚠️ Action 'Action_None' range [74-206] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-235] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-192] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-211] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-229] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-183] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-192] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [194-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [210-230] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-206] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-239] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-221] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-229] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-11] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-227] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-239] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '26' has 1 frames without a visible bounding box.
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

</details>