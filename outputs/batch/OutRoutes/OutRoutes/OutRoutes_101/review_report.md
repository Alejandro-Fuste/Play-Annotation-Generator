# Play-Annotation-Generator Annotation Review — OutRoutes_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_101`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 157
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
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `22` | `22` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `11` | `11` | 21 | START | 21 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `13` | `13` | 21 | START | 21 | 79 |
| ✅ EXACT | `Action_PassBlock` | RT | `19` | `19` | 21 | START | 21 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 21 | START | 21 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `22` | `22` | 21 | START | 21 | 68 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `1` | `1` | 27 | START | 27 | 91 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 27 | END | 27 | 27 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 59 | START | 59 | 68 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `1` | `1` | 92 | START | 92 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `1` | `1` | 103 | START | 103 | 210 |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_None` | 28 | 58 | 31 | inferred_complete_timeline |
| `Action_ThrowPass` | 59 | 68 | 10 | inferred_complete_timeline |
| `Action_None` | 69 | 239 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 218 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunOutRoute` | 27 | 91 | 65 | inferred_complete_timeline |
| `Action_SecureCatch` | 92 | 102 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 210 | 108 | inferred_complete_timeline |
| `Action_BallCarry` | 216 | 220 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 222 | 228 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 239 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 239 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 68 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 71 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 51 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 74 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 176 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 183 | 217 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 219 | 239 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 45 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 79 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 105 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 239 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 79 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 79 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 149 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 157 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 229 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 79 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 88 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 66 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 79 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 207 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 239 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 179 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 110 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 239 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 162 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–109 | 51 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 0–5 | 6 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 24–26 | 3 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 40–41 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 56–79 | 20 | 4 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 58–239 | 143 | 5 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 60–61 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 96–239 | 135 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 97–239 | 143 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 101–239 | 137 | 2 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 101–239 | 120 | 4 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 121–138 | 16 | 3 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 127–128 | 2 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 131–142 | 12 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 154–190 | 17 | 4 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 155–218 | 50 | 2 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 161–163 | 3 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 162–218 | 13 | 3 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 180–239 | 44 | 3 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 188–193 | 6 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 189–192 | 4 | 1 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 195–203 | 9 | 1 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 210–231 | 7 | 2 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 226–239 | 14 | 1 | Undefined position; Undefined team |
| `47` | `60` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |
| `48` | `61` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 101 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-218] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [216-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [222-228] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-179] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-239] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-110] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-79] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-45] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-79] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-105] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-79] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-239] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-149] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-79] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-66] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-79] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-207] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-79] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-74] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-176] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [180-181] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [183-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-68] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-26] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-68] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-79] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-68] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-109] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-218] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-174] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-232] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-239] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-182] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-215] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-228] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-125] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-138] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-142] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-156] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-178] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-186] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-194] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-218] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-163] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-170] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-182] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-218] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-193] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-192] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-203] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-231] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-239] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-239] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>