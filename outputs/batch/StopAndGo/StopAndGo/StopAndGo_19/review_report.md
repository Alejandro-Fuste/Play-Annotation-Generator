# Play-Annotation-Generator Annotation Review — StopAndGo_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_19`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 122
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB1 | offense | `16` | `16` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `2` | `2` |
| ✅ EXACT | `Action_SellStop` | WR3 | offense | `2` | `2` |
| ✅ EXACT | `Action_RunGoRoute` | WR3 | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | QB1 | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | `12` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `16` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 20 | START | 20 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `13` | 26 | START | 37 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `15` | `15` | 26 | START | 26 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 26 | START | 26 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 26 | START | 26 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 26 | START | 26 | 138 |
| ✅ EXACT | `Action_SnapReceive` | QB1 | `16` | `16` | 36 | END | 20 | 36 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `2` | `2` | 38 | START | 38 | 74 |
| ✅ EXACT | `Action_SellStop` | WR3 | `2` | `2` | 75 | START | 75 | 90 |
| ✅ EXACT | `Action_RunGoRoute` | WR3 | `2` | `2` | 91 | START | 91 | 190 |
| ✅ EXACT | `Action_ThrowPass` | QB1 | `16` | `16` | 103 | START | 103 | 113 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 36 | 17 | inferred_complete_timeline |
| `Action_None` | 37 | 102 | 66 | inferred_complete_timeline |
| `Action_ThrowPass` | 103 | 113 | 11 | inferred_complete_timeline |
| `Action_None` | 114 | 128 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 60 | 41 | inferred_complete_timeline |
| `Action_None` | 62 | 213 | 152 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 74 | 55 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 124 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 111 | 92 | inferred_complete_timeline |
| `Action_None` | 117 | 193 | 77 | inferred_complete_timeline |
| `Action_None` | 195 | 239 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_VerticalStem` | 38 | 74 | 37 | inferred_complete_timeline |
| `Action_SellStop` | 75 | 90 | 16 | inferred_complete_timeline |
| `Action_RunGoRoute` | 91 | 190 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 124 | 105 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 138 | 113 | inferred_complete_timeline |
| `Action_PassBlock` | 140 | 162 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 204 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 211 | 239 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 118 | 93 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 175 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 211 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 215 | 220 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 222 | 233 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_BallSnap` | 20 | 36 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 65 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 83 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 121 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 123 | 137 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 144 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 146 | 156 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 163 | 168 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 186 | 189 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 95 | 70 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 129 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 142 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 129 | 104 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 137 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 139 | 147 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 102 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 68 | 49 | inferred_complete_timeline |
| `Action_None` | 75 | 79 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 75 | 56 | inferred_complete_timeline |
| `Action_None` | 79 | 128 | 50 | inferred_complete_timeline |
| `Action_None` | 131 | 156 | 26 | inferred_complete_timeline |
| `Action_None` | 229 | 237 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 190 | 171 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 239 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 93 | 74 | inferred_complete_timeline |
| `Action_None` | 100 | 239 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 180 | 161 | inferred_complete_timeline |
| `Action_None` | 182 | 201 | 20 | inferred_complete_timeline |
| `Action_None` | 206 | 212 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 69–79 | 11 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 96–114 | 9 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 104–234 | 109 | 6 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 115–213 | 99 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 141–153 | 11 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 142–239 | 98 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 146–148 | 3 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 149–237 | 47 | 5 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 179–236 | 46 | 3 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 180–231 | 42 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 210–212 | 3 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 214–217 | 4 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 221–228 | 8 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 228–232 | 5 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (10 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [20–36], lower_priority='Action_PassBlock' annotated_start=26, effective_Action_PassBlock_start=37.
- ⚠️ Action 'Action_None' range [20-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-193] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [91-190] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-124] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-75] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-156] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-124] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-68] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-201] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-190] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [20-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [93-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-121] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [123-137] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [146-156] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-161] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [163-168] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [186-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-129] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-137] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [139-147] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-95] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-118] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-127] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-175] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [178-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [182-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-211] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [215-220] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [222-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-138] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [140-162] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [164-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [172-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-204] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-102] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-161] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-234] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-237] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-236] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-231] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-228] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>