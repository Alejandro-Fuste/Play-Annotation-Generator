# Play-Annotation-Generator Annotation Review — JetSweep_48

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_48`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 29 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `9` | `8` | 30 | START | 30 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `21` | `20` | 59 | START | 59 | 65 |
| ✅ EXACT | `Action_LeadBlock` | RB | `6` | `5` | 60 | START | 60 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE | `8` | `7` | 60 | START | 60 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `14` | 60 | START | 60 | 70 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `17` | `16` | 60 | START | 60 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 60 | START | 71 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `4` | 60 | START | 60 | 91 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 70 | END | 59 | 70 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 76 | START | 76 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `9` | `8` | 85 | START | 85 | 171 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 135 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_SnapReceive` | 59 | 70 | 12 | inferred_complete_timeline |
| `Action_None` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_Toss` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_None` | 85 | 153 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_LeadBlock` | 60 | 135 | 76 | inferred_complete_timeline |
| `Action_None` | 136 | 171 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 152 | 94 | inferred_complete_timeline |
| `Action_None` | 156 | 198 | 43 | inferred_complete_timeline |
| `Action_None` | 201 | 269 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_JetMotion` | 30 | 84 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 171 | 87 | inferred_complete_timeline |
| `Action_BallCarry` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 201 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 210 | 211 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 269 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_SealBlock` | 60 | 212 | 153 | inferred_complete_timeline |
| `Action_SealBlock` | 217 | 221 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 91 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 101 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 135 | 24 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 70 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 135 | 55 | inferred_complete_timeline |
| `Action_None` | 136 | 192 | 57 | inferred_complete_timeline |
| `Action_None` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_BallSnap` | 59 | 65 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 111 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 135 | 21 | inferred_complete_timeline |
| `Action_None` | 136 | 264 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 133 | 74 | inferred_complete_timeline |
| `Action_None` | 138 | 145 | 8 | inferred_complete_timeline |
| `Action_None` | 148 | 161 | 14 | inferred_complete_timeline |
| `Action_None` | 167 | 189 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 89 | 31 | inferred_complete_timeline |
| `Action_None` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_None` | 124 | 127 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 72 | 14 | inferred_complete_timeline |
| `Action_None` | 103 | 114 | 12 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 224 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 72 | 14 | inferred_complete_timeline |
| `Action_None` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_None` | 90 | 114 | 25 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 84 | 26 | inferred_complete_timeline |
| `Action_None` | 87 | 90 | 4 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 255 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 158 | 100 | inferred_complete_timeline |
| `Action_None` | 171 | 248 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 108 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 143 | 85 | inferred_complete_timeline |
| `Action_None` | 145 | 241 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 164 | 106 | inferred_complete_timeline |
| `Action_None` | 167 | 189 | 23 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 256 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 183 | 125 | inferred_complete_timeline |
| `Action_None` | 190 | 240 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–269 | 266 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 64–182 | 46 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 78–269 | 173 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 98–230 | 115 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 178–269 | 68 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 244–269 | 26 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SealBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [59–70], lower_priority='Action_ZoneBlock' annotated_start=60, effective_Action_ZoneBlock_start=71.
- ⚠️ Action 'Action_None' range [59-164] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-189] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-108] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-91] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-135] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-171] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-72] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-114] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-224] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [60-212] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [217-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [186-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [189-201] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [206-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [210-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-256] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-248] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-135] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-145] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-84] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-255] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-183] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-240] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-241] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [59-65] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [69-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-111] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-264] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-89] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-83] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-113] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-207] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>