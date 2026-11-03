# Play-Annotation-Generator Annotation Review — OutAndUp_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_23`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 130
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 109
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_SellOut` | WR | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `0` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `6` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 11 | START | 11 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `14` | `14` | 14 | START | 14 | 46 |
| ✅ EXACT | `Action_PassBlock` | LT | `16` | `16` | 14 | START | 14 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 14 | START | 14 | 26 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `21` | `21` | 14 | START | 18 | 76 |
| ✅ EXACT | `Action_PassBlock` | RT | `9` | `9` | 14 | START | 14 | 83 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 17 | END | 11 | 17 |
| ✅ EXACT | `Action_SellOut` | WR | `0` | `0` | 92 | START | 92 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR | `0` | `0` | 120 | START | 120 | 152 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 138 | START | 138 | 146 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 17 | 7 | inferred_complete_timeline |
| `Action_None` | 18 | 55 | 38 | inferred_complete_timeline |
| `Action_None` | 57 | 137 | 81 | inferred_complete_timeline |
| `Action_ThrowPass` | 138 | 146 | 9 | inferred_complete_timeline |
| `Action_None` | 147 | 239 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 80 | 70 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 239 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 48 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_SellOut` | 92 | 119 | 28 | inferred_complete_timeline |
| `Action_RunGoRoute` | 120 | 152 | 33 | inferred_complete_timeline |
| `Action_RunGoRoute` | 154 | 162 | 9 | inferred_complete_timeline |
| `Action_RunGoRoute` | 164 | 171 | 8 | inferred_complete_timeline |
| `Action_RunGoRoute` | 178 | 209 | 32 | inferred_complete_timeline |
| `Action_RunGoRoute` | 214 | 219 | 6 | inferred_complete_timeline |
| `Action_RunGoRoute` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 38 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 26 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 67 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 239 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 17 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 76 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 46 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 239 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 83 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 147 | 137 | inferred_complete_timeline |
| `Action_None` | 152 | 239 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 66 | 56 | inferred_complete_timeline |
| `Action_None` | 93 | 125 | 33 | inferred_complete_timeline |
| `Action_None` | 143 | 152 | 10 | inferred_complete_timeline |
| `Action_None` | 158 | 185 | 28 | inferred_complete_timeline |
| `Action_None` | 190 | 229 | 40 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 72 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 38 | 28 | inferred_complete_timeline |
| `Action_None` | 59 | 64 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 80 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 42 | 32 | inferred_complete_timeline |
| `Action_None` | 45 | 149 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 170 | 160 | inferred_complete_timeline |
| `Action_None` | 173 | 185 | 13 | inferred_complete_timeline |
| `Action_None` | 188 | 239 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 103 | 93 | inferred_complete_timeline |
| `Action_None` | 108 | 143 | 36 | inferred_complete_timeline |
| `Action_None` | 146 | 174 | 29 | inferred_complete_timeline |
| `Action_None` | 176 | 188 | 13 | inferred_complete_timeline |
| `Action_None` | 191 | 207 | 17 | inferred_complete_timeline |
| `Action_None` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 223 | 9 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |
| `Action_None` | 231 | 237 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 72 | 62 | inferred_complete_timeline |
| `Action_None` | 77 | 207 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 25–239 | 211 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 37–239 | 190 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 37–239 | 173 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 53–239 | 153 | 7 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 77–239 | 161 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 79–239 | 160 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 89–239 | 136 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 109–226 | 46 | 10 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 134–192 | 23 | 4 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 162–239 | 68 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 182–239 | 55 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 220–239 | 15 | 3 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 224–226 | 3 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 224–231 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `21` (C): Annotated start 14 != Inferred start 18
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `0` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 87 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [11–17], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=18.
- ⚠️ Action 'Action_RunGoRoute' range [120-152] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [154-162] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [164-171] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [178-209] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [214-219] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-66] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-125] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-152] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-185] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-229] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-38] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-64] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-143] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-174] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-223] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-239] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-48] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-83] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-207] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-80] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-55] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-239] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-42] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-67] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-57] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-146] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-157] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-218] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-39] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-65] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-135] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-226] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-141] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-121] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-187] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-176] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-193] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-145] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-192] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-223] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-228] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-239] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-231] for track '35' has 1 frames without a visible bounding box.
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

</details>