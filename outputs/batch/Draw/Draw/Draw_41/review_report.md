# Play-Annotation-Generator Annotation Review — Draw_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_41`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 155
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `2` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 31 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 29 | START | 29 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `12` | `11` | 32 | START | 32 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `17` | 32 | START | 32 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `22` | `21` | 32 | START | 32 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `22` | `21` | 32 | START | 32 | 34 |
| ✅ EXACT | `Action_PassBlock` | RT | `8` | `7` | 32 | START | 32 | 34 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 40 | END | 29 | 40 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `13` | `12` | 42 | START | 42 | 66 |
| ✅ EXACT | `Action_BallCarry` | QB | `13` | `12` | 67 | START | 67 | 70 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 108 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 40 | 12 | inferred_complete_timeline |
| `Action_None` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 42 | 66 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 67 | 70 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 96 | 68 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 39 | 11 | inferred_complete_timeline |
| `Action_None` | 44 | 52 | 9 | inferred_complete_timeline |
| `Action_None` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_None` | 64 | 67 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 239 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 239 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 145 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 34 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_None` | 109 | 112 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 34 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 77 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_BallSnap` | 29 | 39 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 34 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 62 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 34 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 122 | 94 | inferred_complete_timeline |
| `Action_None` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 164 | 6 | inferred_complete_timeline |
| `Action_None` | 170 | 183 | 14 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 196 | 9 | inferred_complete_timeline |
| `Action_None` | 201 | 205 | 5 | inferred_complete_timeline |
| `Action_None` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_None` | 221 | 225 | 5 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 34 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 34 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 34 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 72 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 149 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 189 | 161 | inferred_complete_timeline |
| `Action_None` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 239 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 183 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 194 | 166 | inferred_complete_timeline |
| `Action_None` | 209 | 219 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 177 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 65–77 | 6 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 76–239 | 158 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 81–129 | 46 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 90–145 | 36 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 95–96 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 101–102 | 2 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 113–239 | 103 | 5 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 141–142 | 2 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 141–239 | 99 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 141–186 | 10 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 147–183 | 28 | 4 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 153–239 | 86 | 2 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 155–157 | 3 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 160–219 | 26 | 6 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 162–239 | 37 | 6 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 162–239 | 78 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 163–183 | 21 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 169–239 | 71 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 172–239 | 40 | 6 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 172–239 | 54 | 7 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 217–219 | 3 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 226–239 | 14 | 1 | Undefined position; Undefined team |
| `47` | `67` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 230–235 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 97 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [29–39], lower_priority='Action_PassBlock' annotated_start=32, effective_Action_PassBlock_start=40.
- ⚠️ Action 'Action_None' range [29-122] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-183] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-219] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-145] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-96] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-39] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-52] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-67] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-72] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-34] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-177] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-34] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [67-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-194] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [29-39] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-34] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-62] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-222] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-100] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-114] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-129] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-94] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-126] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-201] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-148] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-157] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-220] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-183] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-181] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-201] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-221] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '49' has 2 frames without a visible bounding box.
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

</details>