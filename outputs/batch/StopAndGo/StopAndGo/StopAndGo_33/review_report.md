# Play-Annotation-Generator Annotation Review — StopAndGo_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_33`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 71
- **Ball Tracks:** 0
- **Action Segments:** 175
- **Validation Warnings:** 247
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 156
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_VerticalStem` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SellStop` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | offense | `0` | `0` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `6` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 12 | START | 12 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `12` | `12` | 15 | START | 15 | 47 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | `17` | `17` | 15 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 15 | START | 15 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 15 | START | 15 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 15 | START | 15 | 32 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `11` | `11` | 27 | END | 12 | 27 |
| ✅ EXACT | `Action_VerticalStem` | WR1 | `0` | `0` | 27 | START | 27 | 65 |
| ✅ EXACT | `Action_SellStop` | WR1 | `0` | `0` | 66 | START | 66 | 75 |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | `0` | `0` | 76 | START | 76 | 269 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `11` | `11` | 93 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 56 | 45 | inferred_complete_timeline |
| `Action_None` | 70 | 91 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_VerticalStem` | 27 | 65 | 39 | inferred_complete_timeline |
| `Action_SellStop` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_RunGoRoute` | 76 | 269 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 91 | 80 | inferred_complete_timeline |
| `Action_None` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_None` | 104 | 201 | 98 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 215 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 70 | 59 | inferred_complete_timeline |
| `Action_None` | 73 | 78 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 74 | 63 | inferred_complete_timeline |
| `Action_None` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 47 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 90 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 32 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 40 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 12 | 26 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 20 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 24 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 47 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 58 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 47 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 81 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 47 | 36 | inferred_complete_timeline |
| `Action_None` | 53 | 54 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 28 | 17 | inferred_complete_timeline |
| `Action_None` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_None` | 35 | 47 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 27 | 16 | inferred_complete_timeline |
| `Action_None` | 29 | 33 | 5 | inferred_complete_timeline |
| `Action_None` | 37 | 40 | 4 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 48 | 37 | inferred_complete_timeline |
| `Action_None` | 53 | 58 | 6 | inferred_complete_timeline |
| `Action_None` | 61 | 64 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 102 | 91 | inferred_complete_timeline |
| `Action_None` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_None` | 114 | 218 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 104 | 93 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 145 | 7 | inferred_complete_timeline |
| `Action_None` | 151 | 218 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 105 | 94 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 207 | 94 | inferred_complete_timeline |
| `Action_None` | 217 | 227 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 85 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 98 | 87 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 227 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 98 | 87 | inferred_complete_timeline |
| `Action_None` | 102 | 110 | 9 | inferred_complete_timeline |
| `Action_None` | 112 | 120 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 116 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–74 | 75 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 71–177 | 106 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 80–194 | 110 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 84–87 | 4 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 86–118 | 28 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 90–146 | 28 | 5 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 104–227 | 124 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 106–194 | 57 | 4 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 117–118 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 127–203 | 67 | 4 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 130–191 | 45 | 4 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 132–148 | 14 | 3 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 133–183 | 41 | 4 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 134–207 | 39 | 4 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 135–257 | 118 | 4 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 159–188 | 24 | 4 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 162–176 | 7 | 3 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 164–201 | 36 | 2 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 166–170 | 5 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 174–178 | 4 | 2 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 180–203 | 14 | 2 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 181–185 | 5 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 186–227 | 27 | 2 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 189–198 | 10 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 204–218 | 15 | 1 | Undefined position; Undefined team |
| `49` | `65` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `50` | `68` | Position_Unknown | Team_Unknown | 211–213 | 3 | 1 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 219–221 | 3 | 1 | Undefined position; Undefined team |
| `52` | `74` | Position_Unknown | Team_Unknown | 219–227 | 9 | 1 | Undefined position; Undefined team |
| `53` | `75` | Position_Unknown | Team_Unknown | 222–269 | 48 | 1 | Undefined position; Undefined team |
| `54` | `76` | Position_Unknown | Team_Unknown | 222–269 | 47 | 2 | Undefined position; Undefined team |
| `55` | `77` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `56` | `78` | Position_Unknown | Team_Unknown | 226–227 | 2 | 1 | Undefined position; Undefined team |
| `57` | `79` | Position_Unknown | Team_Unknown | 226–269 | 44 | 1 | Undefined position; Undefined team |
| `58` | `80` | Position_Unknown | Team_Unknown | 228–269 | 42 | 1 | Undefined position; Undefined team |
| `59` | `81` | Position_Unknown | Team_Unknown | 228–269 | 42 | 1 | Undefined position; Undefined team |
| `60` | `82` | Position_Unknown | Team_Unknown | 228–269 | 42 | 1 | Undefined position; Undefined team |
| `61` | `83` | Position_Unknown | Team_Unknown | 228–269 | 42 | 1 | Undefined position; Undefined team |
| `62` | `84` | Position_Unknown | Team_Unknown | 229–269 | 41 | 1 | Undefined position; Undefined team |
| `63` | `85` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `64` | `86` | Position_Unknown | Team_Unknown | 237–246 | 10 | 1 | Undefined position; Undefined team |
| `65` | `87` | Position_Unknown | Team_Unknown | 238–269 | 32 | 1 | Undefined position; Undefined team |
| `66` | `88` | Position_Unknown | Team_Unknown | 238–269 | 32 | 1 | Undefined position; Undefined team |
| `67` | `92` | Position_Unknown | Team_Unknown | 260–269 | 10 | 1 | Undefined position; Undefined team |
| `68` | `95` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |
| `69` | `96` | Position_Unknown | Team_Unknown | 265–266 | 2 | 1 | Undefined position; Undefined team |
| `70` | `97` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (3 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `17` (C)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `11` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 50 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 50 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 100 |
| Missing visible bounding boxes during action | 142 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 48: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '11' has invalid range: start=93, end=74. Clamping end to start.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [12–26], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=27.
- ⚠️ Action 'Action_RunGoRoute' range [76-269] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-100] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-201] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-227] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-28] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-33] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-47] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-227] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-74] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-70] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-78] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-56] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-91] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-102] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-218] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-104] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-218] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-69] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-116] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-48] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-58] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [12-26] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-20] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-24] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-47] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-58] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-106] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-194] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-87] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-105] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-104] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-145] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-194] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-143] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-168] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-203] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-141] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-182] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-141] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-147] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-167] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-187] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-246] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-188] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-176] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-201] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-227] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-198] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-218] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-227] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-269] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-269] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>