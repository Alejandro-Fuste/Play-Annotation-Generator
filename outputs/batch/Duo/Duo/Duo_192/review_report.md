# Play-Annotation-Generator Annotation Review — Duo_192

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_192`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 41
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | offense | `16` | `16` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | `16` | `16` | 132 | START | 133 | 137 |
| ✅ EXACT | `Action_ComboBlock` | C | `18` | `18` | 132 | START | 132 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `18` | `18` | 143 | START | 143 | 148 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 169 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 200 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 160 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 192 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 146 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 154 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 200 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 177 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 186 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 200 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_ComboBlock` | 132 | 142 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 143 | 148 | 6 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 152 | 156 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 162 | 169 | 8 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 187 | 14 | inferred_complete_timeline |
| `Action_None` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_None` | 197 | 200 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 89 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 97 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 133 | 137 | 5 | inferred_complete_timeline |
| `Action_ComboBlock` | 142 | 149 | 8 | inferred_complete_timeline |
| `Action_ComboBlock` | 169 | 169 | 1 | inferred_complete_timeline |
| `Action_None` | 170 | 170 | 1 | inferred_complete_timeline |
| `Action_None` | 172 | 180 | 9 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_None` | 197 | 198 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 194 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 200 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 185 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 189 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 190 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 195 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 200 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 200 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 200 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `22` | Position_Unknown | Team_Unknown | 178–200 | 23 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 178–200 | 21 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 182–200 | 19 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 184–200 | 16 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 189–200 | 12 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 195–200 | 6 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 198–200 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `18` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 71 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-200] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-198] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-200] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-194] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-200] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-160] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-192] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-189] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-190] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-89] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [133-137] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [142-149] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 170, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [170-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-185] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [143-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [152-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [158-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [162-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-187] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-200] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-195] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-200] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-200] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-200] for track '26' has 1 frames without a visible bounding box.
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

</details>