# Play-Annotation-Generator Annotation Review — DeepCross_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_43`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 80
- **Ball Tracks:** 0
- **Action Segments:** 159
- **Validation Warnings:** 249
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 139
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 22 | START | 22 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `15` | `15` | 25 | START | 25 | 111 |
| ✅ EXACT | `Action_PassBlock` | LG | `17` | `17` | 25 | START | 25 | 178 |
| ✅ EXACT | `Action_PassBlock` | RT | `18` | `18` | 25 | START | 25 | 177 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `20` | `20` | 25 | START | 37 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 25 | START | 25 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | `3` | `3` | 36 | START | 36 | 78 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 36 | END | 22 | 36 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 115 | START | 115 | 123 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 36 | 15 | inferred_complete_timeline |
| `Action_None` | 37 | 114 | 78 | inferred_complete_timeline |
| `Action_ThrowPass` | 115 | 123 | 9 | inferred_complete_timeline |
| `Action_None` | 124 | 151 | 28 | inferred_complete_timeline |
| `Action_None` | 154 | 159 | 6 | inferred_complete_timeline |
| `Action_None` | 161 | 174 | 14 | inferred_complete_timeline |
| `Action_None` | 180 | 183 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 178 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 139 | 118 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 159 | 11 | inferred_complete_timeline |
| `Action_None` | 161 | 178 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 36 | 78 | 43 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 80 | 165 | 86 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_None` | 172 | 186 | 15 | inferred_complete_timeline |
| `Action_None` | 188 | 226 | 39 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 74 | 53 | inferred_complete_timeline |
| `Action_None` | 76 | 180 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 53 | 32 | inferred_complete_timeline |
| `Action_None` | 58 | 91 | 34 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 180 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 111 | 87 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 149 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 161 | 174 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 176 | 177 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 178 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 36 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 40 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 180 | 156 | inferred_complete_timeline |
| `Action_PassBlock` | 183 | 185 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 177 | 153 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 144 | 123 | inferred_complete_timeline |
| `Action_None` | 153 | 161 | 9 | inferred_complete_timeline |
| `Action_None` | 163 | 180 | 18 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 65 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 180 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 80 | 59 | inferred_complete_timeline |
| `Action_None` | 82 | 105 | 24 | inferred_complete_timeline |
| `Action_None` | 113 | 239 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 180 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 178 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 180 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 76 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 64 | 43 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 128 | 107 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_None` | 134 | 169 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 62–67 | 6 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 65–148 | 6 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 75–178 | 90 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 79–176 | 97 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 81–148 | 25 | 7 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 85–199 | 115 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 86–178 | 31 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 104–122 | 17 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 155–178 | 12 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 179–200 | 22 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 179–188 | 6 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 179–195 | 9 | 3 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 181–183 | 3 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 181–183 | 3 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 181–239 | 59 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 181–183 | 3 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 181–183 | 3 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 181–188 | 7 | 2 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 181–183 | 3 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 181–183 | 3 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 181–183 | 3 | 1 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 181–188 | 7 | 2 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 181–183 | 3 | 1 | Undefined position; Undefined team |
| `50` | `65` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `51` | `67` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `52` | `68` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `53` | `69` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `54` | `70` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `55` | `71` | Position_Unknown | Team_Unknown | 184–190 | 5 | 2 | Undefined position; Undefined team |
| `56` | `72` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `57` | `73` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `58` | `74` | Position_Unknown | Team_Unknown | 184–190 | 5 | 2 | Undefined position; Undefined team |
| `59` | `75` | Position_Unknown | Team_Unknown | 184–190 | 5 | 2 | Undefined position; Undefined team |
| `60` | `76` | Position_Unknown | Team_Unknown | 184–239 | 52 | 3 | Undefined position; Undefined team |
| `61` | `77` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `62` | `78` | Position_Unknown | Team_Unknown | 186–193 | 7 | 2 | Undefined position; Undefined team |
| `63` | `79` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `64` | `80` | Position_Unknown | Team_Unknown | 186–193 | 7 | 2 | Undefined position; Undefined team |
| `65` | `81` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `66` | `82` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `67` | `83` | Position_Unknown | Team_Unknown | 189–195 | 5 | 2 | Undefined position; Undefined team |
| `68` | `84` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `69` | `85` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `70` | `86` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `71` | `88` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `72` | `89` | Position_Unknown | Team_Unknown | 191–195 | 5 | 1 | Undefined position; Undefined team |
| `73` | `90` | Position_Unknown | Team_Unknown | 191–193 | 3 | 1 | Undefined position; Undefined team |
| `74` | `92` | Position_Unknown | Team_Unknown | 191–193 | 3 | 1 | Undefined position; Undefined team |
| `75` | `94` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `76` | `95` | Position_Unknown | Team_Unknown | 194–239 | 45 | 2 | Undefined position; Undefined team |
| `77` | `96` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `78` | `97` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `79` | `98` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (4 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `20` (C): Annotated start 25 != Inferred start 37
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 59 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 59 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 118 |
| Missing visible bounding boxes during action | 128 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 46: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [22–36], lower_priority='Action_PassBlock' annotated_start=25, effective_Action_PassBlock_start=37.
- ⚠️ Action 'Action_None' range [22-74] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-53] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-178] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [36-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [80-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [167-171] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-64] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-144] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-178] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-65] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-174] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-105] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-169] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-139] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [128-149] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [161-174] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [176-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-178] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [183-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-111] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-100] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-148] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-199] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-96] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-178] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-114] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-122] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-200] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-201] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-206] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.

</details>