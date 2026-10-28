# Play-Annotation-Generator Annotation Review — Draw_88

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_88`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 31 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 32 | START | 32 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `11` | `10` | 35 | START | 35 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `17` | 35 | START | 49 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `19` | 35 | START | 35 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `20` | 35 | START | 35 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `22` | `21` | 35 | START | 35 | 58 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 48 | END | 32 | 48 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `13` | `12` | 53 | START | 53 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `13` | `12` | 74 | START | 74 | 91 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 107 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 53 | 73 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 74 | 91 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 202 | 99 | inferred_complete_timeline |
| `Action_BallCarry` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 237 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 158 | 127 | inferred_complete_timeline |
| `Action_None` | 164 | 183 | 20 | inferred_complete_timeline |
| `Action_None` | 187 | 239 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 106 | 75 | inferred_complete_timeline |
| `Action_None` | 111 | 239 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 98 | 67 | inferred_complete_timeline |
| `Action_None` | 101 | 213 | 113 | inferred_complete_timeline |
| `Action_None` | 215 | 239 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 58 | 27 | inferred_complete_timeline |
| `Action_None` | 61 | 99 | 39 | inferred_complete_timeline |
| `Action_None` | 104 | 117 | 14 | inferred_complete_timeline |
| `Action_None` | 120 | 123 | 4 | inferred_complete_timeline |
| `Action_None` | 132 | 239 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 58 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 90 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 107 | 14 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 239 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 74 | 40 | inferred_complete_timeline |
| `Action_None` | 139 | 157 | 19 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 67 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 94 | 25 | inferred_complete_timeline |
| `Action_None` | 111 | 120 | 10 | inferred_complete_timeline |
| `Action_None` | 123 | 148 | 26 | inferred_complete_timeline |
| `Action_None` | 152 | 172 | 21 | inferred_complete_timeline |
| `Action_None` | 174 | 201 | 28 | inferred_complete_timeline |
| `Action_None` | 207 | 211 | 5 | inferred_complete_timeline |
| `Action_None` | 213 | 220 | 8 | inferred_complete_timeline |
| `Action_None` | 225 | 228 | 4 | inferred_complete_timeline |
| `Action_None` | 236 | 238 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 107 | 73 | inferred_complete_timeline |
| `Action_None` | 108 | 114 | 7 | inferred_complete_timeline |
| `Action_None` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 74 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 107 | 20 | inferred_complete_timeline |
| `Action_None` | 108 | 151 | 44 | inferred_complete_timeline |
| `Action_None` | 157 | 170 | 14 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |
| `Action_None` | 187 | 195 | 9 | inferred_complete_timeline |
| `Action_None` | 200 | 205 | 6 | inferred_complete_timeline |
| `Action_None` | 212 | 216 | 5 | inferred_complete_timeline |
| `Action_None` | 221 | 239 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 71 | 40 | inferred_complete_timeline |
| `Action_None` | 76 | 92 | 17 | inferred_complete_timeline |
| `Action_None` | 105 | 118 | 14 | inferred_complete_timeline |
| `Action_None` | 127 | 239 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 131 | 100 | inferred_complete_timeline |
| `Action_None` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 101 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 97 | 66 | inferred_complete_timeline |
| `Action_None` | 99 | 104 | 6 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_None` | 127 | 131 | 5 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 137 | 106 | inferred_complete_timeline |
| `Action_None` | 139 | 170 | 32 | inferred_complete_timeline |
| `Action_None` | 172 | 218 | 47 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 194 | 163 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 72–74 | 3 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 99–165 | 57 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 110–121 | 8 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 122–137 | 12 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 132–239 | 62 | 10 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 161–239 | 79 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 169–239 | 70 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 178–239 | 62 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 186–239 | 54 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 220–239 | 20 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 226–227 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 176: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [32–48], lower_priority='Action_PassBlock' annotated_start=35, effective_Action_PassBlock_start=49.
- ⚠️ Action 'Action_None' range [32-158] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-183] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-98] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-106] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-118] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-170] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-218] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-170] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-205] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [74-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [95-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-202] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [208-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-194] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-67] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-120] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-220] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-99] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-117] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-74] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-157] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-58] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-111] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-131] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-159] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-195] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-231] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-216] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '33' has 1 frames without a visible bounding box.
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

</details>