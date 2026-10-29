# Play-Annotation-Generator Annotation Review — DeepCross_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_15`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Completion`
- **Result Frame:** 239
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 143
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR1 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | RT | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 8 | START | 8 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 11 | START | 27 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `16` | `16` | 11 | START | 11 | 20 |
| ✅ EXACT | `Action_PassBlock` | LG | `19` | `19` | 11 | START | 11 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 11 | START | 11 | 109 |
| ✅ EXACT | `Action_PassBlock` | LT | `21` | `21` | 11 | START | 11 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR1 | `3` | `3` | 26 | START | 26 | 160 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 26 | END | 8 | 26 |
| ✅ EXACT | `Action_ThrowPass` | RT | `20` | `20` | 122 | START | 122 | 132 |

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
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 26 | 19 | inferred_complete_timeline |
| `Action_None` | 27 | 160 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 162 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 26 | 160 | 135 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 180 | 196 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 160 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 162 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 134 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 162 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 107 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 26 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 109 | 83 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 125 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 134 | 162 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 20 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 73 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 89 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 103 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 109 | 99 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 121 | 9 | inferred_complete_timeline |
| `Action_ThrowPass` | 122 | 132 | 11 | inferred_complete_timeline |
| `Action_None` | 133 | 164 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 118 | 111 | inferred_complete_timeline |
| `Action_None` | 121 | 132 | 12 | inferred_complete_timeline |
| `Action_None` | 162 | 178 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 78 | 71 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 93 | 8 | inferred_complete_timeline |
| `Action_None` | 98 | 103 | 6 | inferred_complete_timeline |
| `Action_None` | 106 | 112 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 164 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 155 | 148 | inferred_complete_timeline |
| `Action_None` | 160 | 164 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 164 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 162 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 239 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 162 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 162 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 162 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 146 | 139 | inferred_complete_timeline |
| `Action_None` | 148 | 160 | 13 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 210 | 25 | inferred_complete_timeline |
| `Action_None` | 215 | 239 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 103–104 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 103–162 | 60 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 107–162 | 56 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 129–174 | 46 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 131–177 | 34 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 133–177 | 44 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 144–147 | 4 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 163–234 | 71 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 163–173 | 11 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 163–169 | 7 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 165–193 | 29 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 165–174 | 10 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 165–224 | 56 | 2 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 165–170 | 6 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 165–211 | 44 | 2 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 165–236 | 66 | 4 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 165–172 | 8 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 165–167 | 3 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 165–207 | 41 | 2 | Undefined position; Undefined team |
| `46` | `56` | Position_Unknown | Team_Unknown | 168–172 | 5 | 1 | Undefined position; Undefined team |
| `47` | `58` | Position_Unknown | Team_Unknown | 176–196 | 12 | 3 | Undefined position; Undefined team |
| `48` | `59` | Position_Unknown | Team_Unknown | 177–202 | 26 | 1 | Undefined position; Undefined team |
| `49` | `60` | Position_Unknown | Team_Unknown | 179–185 | 7 | 1 | Undefined position; Undefined team |
| `50` | `61` | Position_Unknown | Team_Unknown | 230–237 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [8–26], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=27.
- ⚠️ Action 'Action_None' range [8-78] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-93] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-239] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [26-160] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [180-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-155] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-162] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-162] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-160] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-162] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [134-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-164] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-73] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-103] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-134] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-107] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-109] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-162] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-162] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-162] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-160] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-199] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-234] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-173] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-193] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-174] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-175] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-224] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-173] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-211] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-198] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-222] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-236] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-207] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-202] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-237] for track '50' has 2 frames without a visible bounding box.
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

</details>