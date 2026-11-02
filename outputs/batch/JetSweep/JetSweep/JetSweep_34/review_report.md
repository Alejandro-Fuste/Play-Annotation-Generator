# Play-Annotation-Generator Annotation Review — JetSweep_34

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_34`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 28
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `2` | `1` |
| ✅ EXACT | `Action_LeadBlock` | WR | offense | `18` | `17` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `16` | `15` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `19` | `18` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `21` | `20` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `5` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `18` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `4` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 77 |
| ✅ EXACT | `Action_JetMotion` | WR | `2` | `1` | 43 | START | 43 | 103 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 77 | START | 77 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `15` | 78 | START | 78 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 78 | START | 78 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `19` | 78 | START | 78 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 78 | START | 85 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 78 | START | 78 | 140 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 84 | END | 77 | 84 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 97 | START | 97 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `2` | `1` | 104 | START | 104 | 268 |
| ✅ EXACT | `Action_LeadBlock` | WR | `18` | `17` | 129 | START | 129 | 140 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `16` | `15` | 140 | BOUNDARY | 78 | 140 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `19` | `18` | 140 | BOUNDARY | 137 | 140 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `20` | `19` | 140 | BOUNDARY | N/A | 140 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `21` | `20` | 140 | BOUNDARY | N/A | 140 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `5` | `4` | 140 | BOUNDARY | 78 | 140 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_None` | 85 | 96 | 12 | inferred_complete_timeline |
| `Action_Toss` | 97 | 103 | 7 | inferred_complete_timeline |
| `Action_None` | 104 | 198 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_JetMotion` | 43 | 103 | 61 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 268 | 165 | inferred_complete_timeline |
| `Action_BallCarry` | 271 | 299 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 191 | 115 | inferred_complete_timeline |
| `Action_None` | 195 | 197 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 217 | 14 | inferred_complete_timeline |
| `Action_None` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 188 | 112 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 193 | 197 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_LeadBlock` | 129 | 140 | 12 | inferred_complete_timeline |
| `Action_None` | 141 | 254 | 114 | inferred_complete_timeline |
| `Action_None` | 261 | 264 | 4 | inferred_complete_timeline |
| `Action_None` | 267 | 272 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 163 | 87 | inferred_complete_timeline |
| `Action_None` | 166 | 192 | 27 | inferred_complete_timeline |
| `Action_None` | 224 | 261 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 140 | 63 | inferred_complete_timeline |
| `Action_None` | 141 | 257 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 100 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 123 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_None` | 141 | 299 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 115 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 108 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 140 | 63 | inferred_complete_timeline |
| `Action_None` | 141 | 167 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 299 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 100 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 165 | 89 | inferred_complete_timeline |
| `Action_None` | 167 | 208 | 42 | inferred_complete_timeline |
| `Action_None` | 213 | 256 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 207 | 131 | inferred_complete_timeline |
| `Action_None` | 210 | 268 | 59 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 145 | 69 | inferred_complete_timeline |
| `Action_None` | 154 | 299 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 299 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 161 | 85 | inferred_complete_timeline |
| `Action_None` | 169 | 241 | 73 | inferred_complete_timeline |
| `Action_None` | 243 | 267 | 25 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 299 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 233 | 157 | inferred_complete_timeline |
| `Action_None` | 244 | 299 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 257 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 170 | 94 | inferred_complete_timeline |
| `Action_None` | 173 | 299 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 112–207 | 74 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 127–159 | 12 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 155–299 | 145 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 196–256 | 59 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 200–298 | 99 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 206–270 | 46 | 4 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 280–299 | 20 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 286–299 | 14 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 286–299 | 13 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 290–299 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [77–84], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=85.
- ⚠️ Action 'Action_None' range [77-163] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-192] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-268] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [271-299] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-217] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-188] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-257] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-257] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-208] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-256] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-233] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-207] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-170] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-254] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-241] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-267] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-125] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-207] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-203] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-256] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-298] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-215] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-270] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '31' has 1 frames without a visible bounding box.
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

</details>