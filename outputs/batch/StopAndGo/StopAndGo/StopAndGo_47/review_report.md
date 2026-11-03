# Play-Annotation-Generator Annotation Review — StopAndGo_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_47`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 75
- **Ball Tracks:** 0
- **Action Segments:** 223
- **Validation Warnings:** 304
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 9
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 203
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_VerticalStem` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SellStop` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_PumpFake` | Position_Unknown | Team_Unknown | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 21 | START | 21 | 33 |
| ✅ EXACT | `Action_PassBlock` | LT | `12` | `12` | 24 | START | 24 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `13` | 24 | START | 34 | 39 |
| ✅ EXACT | `Action_PassBlock` | RT | `15` | `15` | 24 | START | 24 | 32 |
| ✅ EXACT | `Action_PassBlock` | RG | `16` | `16` | 24 | START | 24 | 47 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `11` | `11` | 33 | END | 21 | 33 |
| ✅ EXACT | `Action_VerticalStem` | WR1 | `0` | `0` | 35 | START | 35 | 52 |
| ✅ EXACT | `Action_SellStop` | WR1 | `0` | `0` | 53 | START | 53 | 79 |
| ✅ EXACT | `Action_PumpFake` | Position_Unknown | `11` | `11` | 62 | START | 62 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | `0` | `0` | 80 | START | 80 | 171 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `11` | `11` | 96 | START | 96 | 104 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 40 | 20 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_VerticalStem` | 35 | 52 | 18 | inferred_complete_timeline |
| `Action_SellStop` | 53 | 79 | 27 | inferred_complete_timeline |
| `Action_RunGoRoute` | 80 | 171 | 92 | inferred_complete_timeline |
| `Action_RunGoRoute` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_RunGoRoute` | 180 | 182 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 269 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 90 | 70 | inferred_complete_timeline |
| `Action_None` | 92 | 97 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 75 | 55 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 84 | 5 | inferred_complete_timeline |
| `Action_None` | 92 | 109 | 18 | inferred_complete_timeline |
| `Action_None` | 117 | 125 | 9 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 156 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 39 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 97 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 111 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 123 | 157 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 179 | 184 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 186 | 190 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 207 | 214 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 229 | 239 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 241 | 246 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 47 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 32 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 47 | 27 | inferred_complete_timeline |
| `Action_None` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_None` | 70 | 75 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 44 | 24 | inferred_complete_timeline |
| `Action_None` | 49 | 57 | 9 | inferred_complete_timeline |
| `Action_None` | 72 | 74 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 40 | 125 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 130 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 133 | 113 | inferred_complete_timeline |
| `Action_None` | 139 | 195 | 57 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 217 | 11 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 111 | 91 | inferred_complete_timeline |
| `Action_None` | 115 | 164 | 50 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 190 | 170 | inferred_complete_timeline |
| `Action_None` | 192 | 204 | 13 | inferred_complete_timeline |
| `Action_None` | 222 | 226 | 5 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 269 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 87 | 67 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 194 | 174 | inferred_complete_timeline |
| `Action_None` | 196 | 205 | 10 | inferred_complete_timeline |
| `Action_None` | 207 | 213 | 7 | inferred_complete_timeline |
| `Action_None` | 216 | 244 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 135 | 115 | inferred_complete_timeline |
| `Action_None` | 137 | 143 | 7 | inferred_complete_timeline |
| `Action_None` | 149 | 152 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 174 | 182 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–125 | 126 | 7 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 9–65 | 44 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 31–127 | 54 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 45–95 | 51 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 61–245 | 176 | 2 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 83–120 | 38 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 85–130 | 46 | 1 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 94–108 | 15 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 112–269 | 131 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 149–264 | 95 | 7 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 151–238 | 22 | 4 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 154–156 | 3 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 169–249 | 6 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 172–173 | 2 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 173–248 | 14 | 2 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 175–242 | 66 | 3 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 175–200 | 23 | 2 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 176–251 | 9 | 3 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 180–251 | 61 | 3 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 182–240 | 43 | 3 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 184–242 | 59 | 1 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 186–195 | 10 | 1 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 186–218 | 33 | 1 | Undefined position; Undefined team |
| `46` | `56` | Position_Unknown | Team_Unknown | 187–211 | 25 | 1 | Undefined position; Undefined team |
| `47` | `59` | Position_Unknown | Team_Unknown | 192–269 | 43 | 9 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 192–194 | 3 | 1 | Undefined position; Undefined team |
| `49` | `61` | Position_Unknown | Team_Unknown | 192–248 | 8 | 3 | Undefined position; Undefined team |
| `50` | `62` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |
| `51` | `63` | Position_Unknown | Team_Unknown | 198–251 | 16 | 3 | Undefined position; Undefined team |
| `52` | `66` | Position_Unknown | Team_Unknown | 206–222 | 17 | 1 | Undefined position; Undefined team |
| `53` | `67` | Position_Unknown | Team_Unknown | 207–243 | 34 | 3 | Undefined position; Undefined team |
| `54` | `69` | Position_Unknown | Team_Unknown | 208–254 | 9 | 2 | Undefined position; Undefined team |
| `55` | `70` | Position_Unknown | Team_Unknown | 208–245 | 30 | 2 | Undefined position; Undefined team |
| `56` | `76` | Position_Unknown | Team_Unknown | 215–217 | 3 | 1 | Undefined position; Undefined team |
| `57` | `78` | Position_Unknown | Team_Unknown | 217–219 | 3 | 1 | Undefined position; Undefined team |
| `58` | `79` | Position_Unknown | Team_Unknown | 217–249 | 20 | 4 | Undefined position; Undefined team |
| `59` | `80` | Position_Unknown | Team_Unknown | 218–229 | 4 | 2 | Undefined position; Undefined team |
| `60` | `83` | Position_Unknown | Team_Unknown | 222–227 | 5 | 2 | Undefined position; Undefined team |
| `61` | `87` | Position_Unknown | Team_Unknown | 224–267 | 9 | 3 | Undefined position; Undefined team |
| `62` | `89` | Position_Unknown | Team_Unknown | 225–240 | 16 | 1 | Undefined position; Undefined team |
| `63` | `90` | Position_Unknown | Team_Unknown | 228–261 | 18 | 2 | Undefined position; Undefined team |
| `64` | `94` | Position_Unknown | Team_Unknown | 235–243 | 9 | 1 | Undefined position; Undefined team |
| `65` | `96` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |
| `66` | `97` | Position_Unknown | Team_Unknown | 237–249 | 7 | 3 | Undefined position; Undefined team |
| `67` | `98` | Position_Unknown | Team_Unknown | 240–248 | 9 | 1 | Undefined position; Undefined team |
| `68` | `101` | Position_Unknown | Team_Unknown | 243–247 | 4 | 2 | Undefined position; Undefined team |
| `69` | `119` | Position_Unknown | Team_Unknown | 248–249 | 2 | 1 | Undefined position; Undefined team |
| `70` | `141` | Position_Unknown | Team_Unknown | 252–269 | 18 | 1 | Undefined position; Undefined team |
| `71` | `143` | Position_Unknown | Team_Unknown | 252–269 | 12 | 3 | Undefined position; Undefined team |
| `72` | `144` | Position_Unknown | Team_Unknown | 253–263 | 6 | 2 | Undefined position; Undefined team |
| `73` | `145` | Position_Unknown | Team_Unknown | 253–269 | 17 | 1 | Undefined position; Undefined team |
| `74` | `155` | Position_Unknown | Team_Unknown | 261–265 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (16 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 55 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 55 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 110 |
| Missing visible bounding boxes during action | 190 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 62: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [21–33], lower_priority='Action_PassBlock' annotated_start=24, effective_Action_PassBlock_start=34.
- ⚠️ Action 'Action_RunGoRoute' range [80-171] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [174-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [180-182] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-111] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-164] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-194] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-205] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-244] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-47] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-109] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-125] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-87] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-190] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-204] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-135] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-125] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-156] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-97] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [123-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [160-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [167-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [171-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [179-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [186-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [207-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [216-218] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [222-223] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [229-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [241-246] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-47] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-130] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-33] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-57] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-195] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-217] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-20] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-27] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-56] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-63] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-113] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-70] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-245] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-120] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-130] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-108] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-158] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-169] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-269] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-164] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-204] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-184] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-242] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-195] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-239] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-211] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-222] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-242] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-195] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-218] for track '45' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-211] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-263] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-251] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-222] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-218] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-227] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-243] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-254] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-227] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-245] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-234] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-240] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-241] for track '63' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-243] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-248] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-258] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>