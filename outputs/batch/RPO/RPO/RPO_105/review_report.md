# Play-Annotation-Generator Annotation Review — RPO_105

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_105`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 151
- **Validation Warnings:** 150
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunOutRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 132
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_PullBall` | RB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `14` | 24 | START | 24 | 38 |
| ✅ EXACT | `Action_ZoneBlock` | C | `18` | `18` | 24 | START | 24 | 50 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 24 | START | 24 | 32 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 24 | START | 24 | 44 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 24 | START | 24 | 41 |
| ✅ EXACT | `Action_ReadDefender` | QB | `17` | `17` | 36 | START | 36 | 44 |
| ✅ EXACT | `Action_PullBall` | RB | `16` | `16` | 70 | START | 70 | 79 |
| ✅ EXACT | `Action_ThrowPass` | RB | `16` | `16` | 92 | START | 92 | 97 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 35 | 13 | inferred_complete_timeline |
| `Action_ReadDefender` | 36 | 44 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 69 | 47 | inferred_complete_timeline |
| `Action_PullBall` | 70 | 79 | 10 | inferred_complete_timeline |
| `Action_None` | 80 | 91 | 12 | inferred_complete_timeline |
| `Action_ThrowPass` | 92 | 97 | 6 | inferred_complete_timeline |
| `Action_None` | 98 | 269 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 65 | 43 | inferred_complete_timeline |
| `Action_None` | 68 | 269 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 74 | 52 | inferred_complete_timeline |
| `Action_None` | 119 | 169 | 51 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |
| `Action_None` | 194 | 203 | 10 | inferred_complete_timeline |
| `Action_None` | 208 | 222 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 23 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 41 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 23 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 32 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 23 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 50 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 23 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 44 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 23 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 38 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 70 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 40 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 57 | 35 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 68 | 76 | 9 | inferred_complete_timeline |
| `Action_None` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_None` | 94 | 99 | 6 | inferred_complete_timeline |
| `Action_None` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 125 | 182 | 58 | inferred_complete_timeline |
| `Action_None` | 186 | 269 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 42 | 20 | inferred_complete_timeline |
| `Action_None` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 228 | 107 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 77 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 245 | 223 | inferred_complete_timeline |
| `Action_None` | 247 | 269 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 122 | 100 | inferred_complete_timeline |
| `Action_None` | 126 | 161 | 36 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 225 | 60 | inferred_complete_timeline |
| `Action_None` | 228 | 245 | 18 | inferred_complete_timeline |
| `Action_None` | 252 | 258 | 7 | inferred_complete_timeline |
| `Action_None` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 149 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 46 | 24 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_None` | 65 | 72 | 8 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 97 | 8 | inferred_complete_timeline |
| `Action_None` | 109 | 116 | 8 | inferred_complete_timeline |
| `Action_None` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 141 | 5 | inferred_complete_timeline |
| `Action_None` | 143 | 164 | 22 | inferred_complete_timeline |
| `Action_None` | 166 | 211 | 46 | inferred_complete_timeline |
| `Action_None` | 214 | 269 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 66–269 | 204 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 77–269 | 183 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 104–197 | 60 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 124–137 | 7 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 128–131 | 4 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 132–269 | 138 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 132–185 | 54 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 136–269 | 100 | 5 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 137–225 | 56 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 137–238 | 52 | 10 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 157–262 | 104 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 162–163 | 2 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 170–269 | 95 | 4 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 183–269 | 87 | 1 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 191–256 | 58 | 4 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 195–197 | 3 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 212–213 | 2 | 1 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 213–239 | 15 | 3 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 217–262 | 35 | 6 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 243–269 | 23 | 4 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 245–249 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 107 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [23-65] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-269] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-245] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-74] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-203] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-222] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-122] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-161] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-225] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-245] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-258] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-41] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-77] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-42] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-228] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-70] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-164] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-211] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [36-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-32] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-44] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-109] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-128] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-185] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-147] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-227] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-246] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-147] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-182] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-225] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-190] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-212] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-257] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-212] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-245] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-269] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-219] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-246] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-256] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-239] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-226] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-244] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '42' has 1 frames without a visible bounding box.
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

</details>