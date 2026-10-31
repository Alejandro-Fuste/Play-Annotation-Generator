# Play-Annotation-Generator Annotation Review — Hitch_22

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_22`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 54
- **Ball Tracks:** 0
- **Action Segments:** 143
- **Validation Warnings:** 172
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 122
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunHitchRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 25 | START | 25 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `11` | `11` | 28 | START | 28 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `16` | `16` | 28 | START | 28 | 38 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | `17` | `17` | 28 | START | N/A | N/A |
| ✅ EXACT | `Action_PassBlock` | LG | `18` | `18` | 28 | START | 28 | 39 |
| ✅ EXACT | `Action_PassBlock` | LT | `19` | `19` | 28 | START | 28 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunHitchRoute` | WR2 | `1` | `1` | 39 | START | 39 | 80 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 39 | END | 25 | 39 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 107 | START | 107 | 109 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `1` | `1` | 146 | START | 146 | 159 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 39 | 15 | inferred_complete_timeline |
| `Action_None` | 40 | 106 | 67 | inferred_complete_timeline |
| `Action_ThrowPass` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_None` | 148 | 269 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 24 | 17 | inferred_complete_timeline |
| `Action_None` | 25 | 61 | 37 | inferred_complete_timeline |
| `Action_None` | 63 | 65 | 3 | inferred_complete_timeline |
| `Action_None` | 67 | 78 | 12 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 59 | 35 | inferred_complete_timeline |
| `Action_None` | 64 | 68 | 5 | inferred_complete_timeline |
| `Action_None` | 73 | 74 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 39 | 80 | 42 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 83 | 114 | 32 | inferred_complete_timeline |
| `Action_None` | 115 | 145 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 146 | 159 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 170 | 146 | inferred_complete_timeline |
| `Action_None` | 173 | 264 | 92 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 32 | 8 | inferred_complete_timeline |
| `Action_None` | 34 | 36 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 31 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 39 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 33 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 38 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 60 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 40 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 44 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 38 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 32 | 8 | inferred_complete_timeline |
| `Action_None` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 32 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 32 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 167 | 143 | inferred_complete_timeline |
| `Action_None` | 169 | 183 | 15 | inferred_complete_timeline |
| `Action_None` | 186 | 233 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 255 | 231 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 269 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 269 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 139 | 115 | inferred_complete_timeline |
| `Action_None` | 146 | 149 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 247 | 223 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 269 | 245 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 54–122 | 31 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 65–69 | 4 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 77–79 | 3 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 78–269 | 192 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 85–269 | 185 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 93–106 | 9 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 100–102 | 3 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 109–269 | 161 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 114–135 | 8 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 138–269 | 122 | 4 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 138–151 | 9 | 2 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 146–150 | 5 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 151–268 | 102 | 4 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 160–207 | 45 | 2 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 160–256 | 88 | 4 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 166–168 | 3 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 175–207 | 14 | 2 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 177–269 | 91 | 3 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 179–184 | 6 | 1 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 180–200 | 18 | 3 | Undefined position; Undefined team |
| `43` | `50` | Position_Unknown | Team_Unknown | 183–237 | 48 | 6 | Undefined position; Undefined team |
| `44` | `51` | Position_Unknown | Team_Unknown | 183–269 | 84 | 3 | Undefined position; Undefined team |
| `45` | `53` | Position_Unknown | Team_Unknown | 190–269 | 72 | 4 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 194–198 | 5 | 1 | Undefined position; Undefined team |
| `47` | `56` | Position_Unknown | Team_Unknown | 199–221 | 19 | 3 | Undefined position; Undefined team |
| `48` | `58` | Position_Unknown | Team_Unknown | 220–240 | 9 | 2 | Undefined position; Undefined team |
| `49` | `61` | Position_Unknown | Team_Unknown | 233–247 | 10 | 3 | Undefined position; Undefined team |
| `50` | `62` | Position_Unknown | Team_Unknown | 233–269 | 25 | 3 | Undefined position; Undefined team |
| `51` | `66` | Position_Unknown | Team_Unknown | 255–269 | 15 | 1 | Undefined position; Undefined team |
| `52` | `67` | Position_Unknown | Team_Unknown | 256–258 | 3 | 1 | Undefined position; Undefined team |
| `53` | `69` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (3 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `17` (C)
- ⚠️ Ambiguous match for action `Action_RunHitchRoute` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 106 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [25–33], lower_priority='Action_PassBlock' annotated_start=28, effective_Action_PassBlock_start=34.
- ⚠️ Action 'Action_None' range [25-170] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-264] for track '0' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [39-80] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [146-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-59] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-32] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-255] for track '4' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-139] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-32] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-32] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-40] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-247] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-38] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [107-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-167] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-233] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-60] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [25-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-39] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-31] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-32] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-24] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-61] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-65] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-269] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-164] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-202] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-229] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-268] for track '35' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-207] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-233] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-186] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-250] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-257] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-191] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-214] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-228] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-194] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-252] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-259] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-221] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-266] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-269] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '53' has 1 frames without a visible bounding box.
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

</details>