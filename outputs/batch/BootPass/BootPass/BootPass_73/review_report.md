# Play-Annotation-Generator Annotation Review — BootPass_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_73`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Comp.`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 104
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_RunFlatRoute` | TE | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `34` | `27` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 44 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 45 | START | 45 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `14` | `14` | 54 | START | 63 | 86 |
| ✅ EXACT | `Action_RunBlock` | RT | `17` | `17` | 54 | START | 54 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `19` | `19` | 54 | START | 54 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `20` | `20` | 54 | START | 54 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `21` | `21` | 54 | START | 54 | 82 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 62 | END | 45 | 62 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `9` | `9` | 70 | START | 70 | 91 |
| ✅ EXACT | `Action_BootAway` | QB | `9` | `9` | 92 | START | 92 | 128 |
| ✅ EXACT | `Action_RunFlatRoute` | TE | `7` | `7` | 96 | START | 96 | 132 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 132 | START | 132 | 145 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `34` | `27` | 192 | START | 192 | 214 |

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
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 62 | 18 | inferred_complete_timeline |
| `Action_None` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_FakeHandoff` | 70 | 91 | 22 | inferred_complete_timeline |
| `Action_BootAway` | 92 | 128 | 37 | inferred_complete_timeline |
| `Action_None` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_ThrowPass` | 132 | 145 | 14 | inferred_complete_timeline |
| `Action_None` | 146 | 152 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 104 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 168 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 125 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 141 | 97 | inferred_complete_timeline |
| `Action_None` | 143 | 239 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 96 | 132 | 37 | inferred_complete_timeline |
| `Action_None` | 133 | 202 | 70 | inferred_complete_timeline |
| `Action_None` | 206 | 211 | 6 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 218 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 96 | 43 | inferred_complete_timeline |
| `Action_RunBlock` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 135 | 147 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 168 | 181 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 82 | 29 | inferred_complete_timeline |
| `Action_RunBlock` | 87 | 106 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_BallSnap` | 45 | 62 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 63 | 86 | 24 | inferred_complete_timeline |
| `Action_RunBlock` | 122 | 125 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 107 | 54 | inferred_complete_timeline |
| `Action_RunBlock` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 113 | 115 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_RunBlock` | 54 | 112 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 129 | 85 | inferred_complete_timeline |
| `Action_None` | 132 | 139 | 8 | inferred_complete_timeline |
| `Action_None` | 146 | 190 | 45 | inferred_complete_timeline |
| `Action_None` | 192 | 205 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 119 | 75 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 142 | 4 | inferred_complete_timeline |
| `Action_None` | 146 | 239 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 115 | 71 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 229 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 107 | 63 | inferred_complete_timeline |
| `Action_None` | 109 | 116 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 103 | 59 | inferred_complete_timeline |
| `Action_None` | 121 | 204 | 84 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 104 | 60 | inferred_complete_timeline |
| `Action_None` | 136 | 141 | 6 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 143 | 99 | inferred_complete_timeline |
| `Action_None` | 145 | 239 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 213 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 77 | 33 | inferred_complete_timeline |
| `Action_None` | 79 | 239 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 239 | 195 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 116 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 13–52 | 40 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 72–239 | 113 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 116–239 | 94 | 7 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 122–158 | 37 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 123–151 | 15 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 135–221 | 87 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 141–239 | 55 | 5 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 145–239 | 95 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 152–172 | 15 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 157–239 | 79 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 162–163 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 165–179 | 11 | 3 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 182–239 | 45 | 3 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 189–239 | 51 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 207–239 | 32 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 214–239 | 26 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 233–239 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (9 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [45–62], lower_priority='Action_RunBlock' annotated_start=54, effective_Action_RunBlock_start=63.
- ⚠️ Action 'Action_None' range [45-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-139] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-190] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-104] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-119] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-107] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-116] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-115] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-229] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-202] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-213] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-204] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [63-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [122-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-141] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [54-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [54-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [102-107] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [109-110] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [130-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [135-147] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [168-181] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [187-190] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [192-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [199-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [54-107] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [109-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [113-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [54-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [87-106] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [161-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-52] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-146] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-189] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-158] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-138] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-221] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-194] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-231] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '36' has 1 frames without a visible bounding box.
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

</details>