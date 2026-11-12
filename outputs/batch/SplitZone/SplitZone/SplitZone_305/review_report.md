# Play-Annotation-Generator Annotation Review — SplitZone_305

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_305`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 58
- **Ball Tracks:** 0
- **Action Segments:** 132
- **Validation Warnings:** 166
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | SAF1 | defense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB2 | defense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_PressEdge` | DE2 | defense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | CB2 | defense | `14` | `14` |
| ✅ EXACT | `Action_ReadEdgeDefender` | CB2 | defense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | CB2 | defense | `14` | `14` |
| ✅ EXACT | `Action_BallCarry` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | SAF1 | `15` | `15` | 85 | START | 85 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB2 | `4` | `4` | 90 | START | 90 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `11` | 93 | START | 93 | 134 |
| ✅ EXACT | `Action_ZoneBlock` | C | `17` | `17` | 93 | START | 93 | 112 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 93 | START | 93 | 134 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `21` | `21` | 93 | START | 93 | 124 |
| ✅ EXACT | `Action_PressEdge` | DE2 | `7` | `7` | 94 | START | 94 | 153 |
| ✅ EXACT | `Action_SnapReceive` | CB2 | `14` | `14` | 97 | END | 85 | 97 |
| ✅ EXACT | `Action_ReadEdgeDefender` | CB2 | `14` | `14` | 100 | START | 100 | 110 |
| ✅ EXACT | `Action_Handoff` | CB2 | `14` | `14` | 115 | START | 115 | 122 |
| ✅ EXACT | `Action_BallCarry` | C | `17` | `17` | 124 | START | 124 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | `21` | `21` | 125 | START | 125 | 139 |

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
- **Visible Frames:** 0–192
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 168 | 84 | inferred_complete_timeline |
| `Action_None` | 174 | 192 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 144 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 168 | 84 | inferred_complete_timeline |
| `Action_None` | 191 | 195 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 120 | 36 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 118 | 34 | inferred_complete_timeline |
| `Action_None` | 124 | 191 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 106 | 22 | inferred_complete_timeline |
| `Action_None` | 191 | 195 | 5 | inferred_complete_timeline |
| `Action_None` | 197 | 206 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 78 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 92 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 124 | 32 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 125 | 139 | 15 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 141 | 144 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 170 | 22 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 112 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 124 | 189 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 134 | 42 | inferred_complete_timeline |
| `Action_None` | 135 | 149 | 15 | inferred_complete_timeline |
| `Action_None` | 151 | 191 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 134 | 42 | inferred_complete_timeline |
| `Action_None` | 135 | 196 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 138 | 54 | inferred_complete_timeline |
| `Action_None` | 191 | 195 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PressEdge` | 94 | 153 | 60 | inferred_complete_timeline |
| `Action_None` | 154 | 169 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 149 | 65 | inferred_complete_timeline |
| `Action_None` | 155 | 160 | 6 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 92 | 8 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 171 | 87 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_SplitBlock` | 90 | 117 | 28 | inferred_complete_timeline |
| `Action_SplitBlock` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 191 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 176 | 92 | inferred_complete_timeline |
| `Action_None` | 178 | 183 | 6 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_SnapReceive` | 85 | 97 | 13 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 100 | 110 | 11 | inferred_complete_timeline |
| `Action_None` | 111 | 114 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_None` | 123 | 164 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 162 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_BallSnap` | 85 | 90 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 92 | 97 | 6 | inferred_complete_timeline |
| `Action_None` | 98 | 157 | 60 | inferred_complete_timeline |
| `Action_None` | 159 | 192 | 34 | inferred_complete_timeline |
| `Action_None` | 195 | 214 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 156 | 72 | inferred_complete_timeline |
| `Action_None` | 195 | 359 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–195 | 196 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 34–189 | 74 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 114–195 | 80 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 127–186 | 60 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 129–160 | 32 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 140–155 | 16 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 140–195 | 29 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 148–149 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 173–191 | 19 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 186–191 | 6 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 189–191 | 3 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 193–195 | 3 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 193–195 | 3 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 196–200 | 5 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 196–235 | 40 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 196–212 | 17 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 196–358 | 159 | 2 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 196–203 | 8 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 196–296 | 99 | 2 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 197–270 | 73 | 2 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 200–220 | 19 | 2 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 201–266 | 66 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 202–210 | 9 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 210–359 | 130 | 3 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 223–359 | 137 | 1 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 253–359 | 107 | 1 | Undefined position; Undefined team |
| `50` | `66` | Position_Unknown | Team_Unknown | 259–359 | 101 | 1 | Undefined position; Undefined team |
| `51` | `67` | Position_Unknown | Team_Unknown | 294–359 | 66 | 1 | Undefined position; Undefined team |
| `52` | `68` | Position_Unknown | Team_Unknown | 302–359 | 56 | 2 | Undefined position; Undefined team |
| `53` | `69` | Position_Unknown | Team_Unknown | 307–347 | 40 | 2 | Undefined position; Undefined team |
| `54` | `72` | Position_Unknown | Team_Unknown | 318–359 | 42 | 1 | Undefined position; Undefined team |
| `55` | `74` | Position_Unknown | Team_Unknown | 339–345 | 4 | 2 | Undefined position; Undefined team |
| `56` | `76` | Position_Unknown | Team_Unknown | 350–359 | 10 | 1 | Undefined position; Undefined team |
| `57` | `81` | Position_Unknown | Team_Unknown | 356–359 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 37 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 37 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 74 |
| Missing visible bounding boxes during action | 90 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 612: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [85-118] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-191] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [90-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [120-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-206] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-156] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-359] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-196] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-168] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-192] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [85-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-192] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-214] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [124-189] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-176] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-195] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-191] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [125-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [141-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-189] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-195] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-155] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-191] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-235] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-212] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-240] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-358] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-203] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-239] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-296] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-208] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-270] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-220] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-266] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-240] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-283] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-309] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-347] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '55' has 1 frames without a visible bounding box.
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

</details>