# Play-Annotation-Generator Annotation Review — Hitch_54

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_54`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_RunHitchRoute` | WR4 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_BallCarry` | WR4 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 14 | START | 14 | 32 |
| ✅ EXACT | `Action_PassBlock` | LG | `11` | `11` | 17 | START | 17 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 17 | START | 17 | 50 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `21` | `21` | 17 | START | 33 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `4` | 17 | START | 17 | 170 |
| ✅ EXACT | `Action_PassBlock` | RT | `5` | `5` | 17 | START | 17 | 149 |
| ✅ EXACT | `Action_RunHitchRoute` | WR4 | `1` | `1` | 32 | START | 32 | 106 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 32 | END | 14 | 32 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 80 | START | 80 | 91 |
| ✅ EXACT | `Action_BallCarry` | WR4 | `1` | `1` | 138 | START | 138 | 164 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 14 | 32 | 19 | inferred_complete_timeline |
| `Action_None` | 33 | 79 | 47 | inferred_complete_timeline |
| `Action_ThrowPass` | 80 | 91 | 12 | inferred_complete_timeline |
| `Action_None` | 92 | 210 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 161 | 148 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 175 | 193 | 19 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 145 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 187 | 174 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 32 | 106 | 75 | inferred_complete_timeline |
| `Action_None` | 107 | 137 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 164 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 170 | 154 | inferred_complete_timeline |
| `Action_PassBlock` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 190 | 192 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 197 | 205 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 127 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 14 | 32 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 66 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 50 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 84 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 139 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 149 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 172 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 149 | 133 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 93 | 80 | inferred_complete_timeline |
| `Action_None` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 118 | 9 | inferred_complete_timeline |
| `Action_None` | 122 | 124 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 92 | 79 | inferred_complete_timeline |
| `Action_None` | 97 | 118 | 22 | inferred_complete_timeline |
| `Action_None` | 205 | 209 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 54 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 89 | 76 | inferred_complete_timeline |
| `Action_None` | 92 | 210 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 146 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 187 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 62 | 49 | inferred_complete_timeline |
| `Action_None` | 68 | 172 | 105 | inferred_complete_timeline |
| `Action_None` | 174 | 210 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 171 | 158 | inferred_complete_timeline |
| `Action_None` | 176 | 183 | 8 | inferred_complete_timeline |
| `Action_None` | 185 | 193 | 9 | inferred_complete_timeline |
| `Action_None` | 195 | 210 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 61–95 | 30 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 69–210 | 123 | 4 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 110–120 | 11 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 124–210 | 87 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 128–195 | 68 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 155–162 | 7 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 175–210 | 26 | 4 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 177–202 | 12 | 4 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 179–181 | 3 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 193–195 | 3 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `21` (C): Annotated start 17 != Inferred start 33
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [14–32], lower_priority='Action_PassBlock' annotated_start=17, effective_Action_PassBlock_start=33.
- ⚠️ Action 'Action_None' range [14-187] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-164] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-170] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [172-176] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [190-192] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [197-205] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [209-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-54] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-145] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-193] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-62] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-172] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-127] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-146] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-93] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-118] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-139] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [152-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-167] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-193] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '33' has 1 frames without a visible bounding box.
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

</details>