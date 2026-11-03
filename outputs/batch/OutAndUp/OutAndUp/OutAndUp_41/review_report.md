# Play-Annotation-Generator Annotation Review — OutAndUp_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_41`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 137
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 116
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_SellOut` | TE3 | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | TE3 | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `6` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 12 | START | 12 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `12` | `12` | 15 | START | 15 | 138 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `17` | `17` | 15 | START | 20 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 15 | START | 15 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `8` | 15 | START | 15 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `9` | 15 | START | 15 | 131 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 19 | END | 12 | 19 |
| ✅ EXACT | `Action_SellOut` | TE3 | `6` | `6` | 72 | START | 72 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | TE3 | `6` | `6` | 89 | START | 89 | 234 |
| ✅ EXACT | `Action_ThrowPass` | QB | `21` | `21` | 106 | START | 106 | 117 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 12 | 19 | 8 | inferred_complete_timeline |
| `Action_None` | 20 | 63 | 44 | inferred_complete_timeline |
| `Action_None` | 65 | 77 | 13 | inferred_complete_timeline |
| `Action_None` | 82 | 105 | 24 | inferred_complete_timeline |
| `Action_ThrowPass` | 106 | 117 | 12 | inferred_complete_timeline |
| `Action_None` | 118 | 191 | 74 | inferred_complete_timeline |
| `Action_None` | 196 | 269 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 193 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 134 | 123 | inferred_complete_timeline |
| `Action_None` | 138 | 145 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 125 | 114 | inferred_complete_timeline |
| `Action_None` | 127 | 143 | 17 | inferred_complete_timeline |
| `Action_None` | 150 | 186 | 37 | inferred_complete_timeline |
| `Action_None` | 191 | 211 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 132 | 121 | inferred_complete_timeline |
| `Action_None` | 144 | 198 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_SellOut` | 72 | 88 | 17 | inferred_complete_timeline |
| `Action_RunGoRoute` | 89 | 234 | 146 | inferred_complete_timeline |
| `Action_RunGoRoute` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_RunGoRoute` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 131 | 117 | inferred_complete_timeline |
| `Action_PassBlock` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 142 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 145 | 150 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 164 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 182 | 189 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 43 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 118 | 65 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 133 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 12 | 19 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 103 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 138 | 124 | inferred_complete_timeline |
| `Action_PassBlock` | 144 | 151 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 164 | 212 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 28 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 105 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 64 | 53 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 177 | 107 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 52 | 41 | inferred_complete_timeline |
| `Action_None` | 54 | 60 | 7 | inferred_complete_timeline |
| `Action_None` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_None` | 75 | 78 | 4 | inferred_complete_timeline |
| `Action_None` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 230 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 63 | 52 | inferred_complete_timeline |
| `Action_None` | 65 | 73 | 9 | inferred_complete_timeline |
| `Action_None` | 75 | 81 | 7 | inferred_complete_timeline |
| `Action_None` | 84 | 103 | 20 | inferred_complete_timeline |
| `Action_None` | 105 | 123 | 19 | inferred_complete_timeline |
| `Action_None` | 127 | 149 | 23 | inferred_complete_timeline |
| `Action_None` | 164 | 219 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 80 | 69 | inferred_complete_timeline |
| `Action_None` | 82 | 251 | 170 | inferred_complete_timeline |
| `Action_None` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 152 | 141 | inferred_complete_timeline |
| `Action_None` | 154 | 194 | 41 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_None` | 203 | 212 | 10 | inferred_complete_timeline |
| `Action_None` | 214 | 217 | 4 | inferred_complete_timeline |
| `Action_None` | 221 | 224 | 4 | inferred_complete_timeline |
| `Action_None` | 230 | 269 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 269 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 120 | 109 | inferred_complete_timeline |
| `Action_None` | 127 | 133 | 7 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 144 | 133 | inferred_complete_timeline |
| `Action_None` | 146 | 150 | 5 | inferred_complete_timeline |
| `Action_None` | 156 | 192 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 150 | 139 | inferred_complete_timeline |
| `Action_None` | 153 | 160 | 8 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_None` | 194 | 198 | 5 | inferred_complete_timeline |
| `Action_None` | 205 | 216 | 12 | inferred_complete_timeline |
| `Action_None` | 221 | 269 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 150 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 122 | 111 | inferred_complete_timeline |
| `Action_None` | 128 | 154 | 27 | inferred_complete_timeline |
| `Action_None` | 159 | 166 | 8 | inferred_complete_timeline |
| `Action_None` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 190 | 196 | 7 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 87–211 | 83 | 7 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 127–207 | 80 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 153–269 | 115 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 158–261 | 104 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 173–205 | 33 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 174–195 | 18 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 192–206 | 13 | 3 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 202–205 | 4 | 1 | Undefined position; Undefined team |
| `30` | `49` | Position_Unknown | Team_Unknown | 264–266 | 3 | 1 | Undefined position; Undefined team |
| `31` | `53` | Position_Unknown | Team_Unknown | 269–269 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (3 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `17` (C): Annotated start 15 != Inferred start 20
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (6 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 105 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [12–19], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=20.
- ⚠️ Action 'Action_None' range [12-150] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-144] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-132] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-198] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-193] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-120] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-133] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [89-234] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [237-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [255-269] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-80] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-251] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-28] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-44] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-60] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-77] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-105] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-131] for track '9' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [134-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [145-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-164] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [182-189] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-194] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-269] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-138] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [144-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [164-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-230] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-154] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-160] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-216] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-269] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-103] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-125] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-143] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-186] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-211] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-73] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-103] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-149] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-219] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-43] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-51] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [128-133] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-77] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-211] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-194] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-261] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '30' has 1 frames without a visible bounding box.
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