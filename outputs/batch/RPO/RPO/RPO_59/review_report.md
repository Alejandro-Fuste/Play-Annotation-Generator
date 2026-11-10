# Play-Annotation-Generator Annotation Review — RPO_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_59`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSeamRoute` | actor_track_id `2` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 104 | START | 128 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 104 | START | 104 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `16` | `16` | 104 | START | 126 | 143 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `21` | `21` | 104 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `7` | 104 | START | 104 | 161 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `12` | 112 | START | 112 | 127 |
| ✅ EXACT | `Action_PullBall` | QB | `12` | `12` | 128 | START | 128 | 139 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 155 | START | 155 | 166 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 111 | 9 | inferred_complete_timeline |
| `Action_ReadDefender` | 112 | 127 | 16 | inferred_complete_timeline |
| `Action_PullBall` | 128 | 139 | 12 | inferred_complete_timeline |
| `Action_None` | 140 | 154 | 15 | inferred_complete_timeline |
| `Action_ThrowPass` | 155 | 166 | 12 | inferred_complete_timeline |
| `Action_None` | 167 | 249 | 83 | inferred_complete_timeline |
| `Action_None` | 252 | 269 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 121 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 269 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 269 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 269 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 124 | 22 | inferred_complete_timeline |
| `Action_None` | 127 | 140 | 14 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 269 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 161 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 166 | 4 | inferred_complete_timeline |
| `Action_None` | 168 | 269 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 104 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 144 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 161 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 177 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 134 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 160 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 143 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 161 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 188 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 269 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_None` | 127 | 134 | 8 | inferred_complete_timeline |
| `Action_None` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_None` | 146 | 149 | 4 | inferred_complete_timeline |
| `Action_None` | 151 | 160 | 10 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 177 | 6 | inferred_complete_timeline |
| `Action_None` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_None` | 241 | 250 | 10 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 111 | 9 | inferred_complete_timeline |
| `Action_None` | 117 | 124 | 8 | inferred_complete_timeline |
| `Action_None` | 127 | 134 | 8 | inferred_complete_timeline |
| `Action_None` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 155 | 161 | 7 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 177 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 134 | 32 | inferred_complete_timeline |
| `Action_None` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_None` | 184 | 230 | 47 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 266 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 143 | 41 | inferred_complete_timeline |
| `Action_None` | 145 | 182 | 38 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 269 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 269 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 269 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 192 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 231 | 129 | inferred_complete_timeline |
| `Action_None` | 233 | 235 | 3 | inferred_complete_timeline |
| `Action_None` | 239 | 244 | 6 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 133–159 | 16 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 142–189 | 28 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 152–269 | 116 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 173–227 | 30 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 188–205 | 11 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 196–210 | 13 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 197–200 | 4 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 213–269 | 55 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 229–235 | 5 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 237–268 | 32 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 238–267 | 9 | 3 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 243–268 | 23 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 246–269 | 24 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 254–257 | 4 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 257–267 | 7 | 2 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 269–269 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (LG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 106 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=104, end=103. Clamping end to start.
- ⚠️ Action 'Action_None' range [103-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-182] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-192] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-161] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-269] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-231] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-249] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 103, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [103-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-160] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '15' starts at frame 104, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [104-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-144] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-161] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-164] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 103, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [103-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [126-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 103, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [103-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-250] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-111] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 103, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [103-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 103, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [103-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-222] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-257] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-268] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-260] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-269] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-261] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '39' has 1 frames without a visible bounding box.
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

</details>