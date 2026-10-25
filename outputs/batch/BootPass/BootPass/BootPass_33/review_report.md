# Play-Annotation-Generator Annotation Review — BootPass_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_33`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Comp.`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_RunBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_SecureCatch` | TE2 | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 36 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 24 | START | 24 | 30 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 30 | END | 24 | 30 |
| ✅ EXACT | `Action_RunBlock` | C | `14` | `14` | 37 | START | 37 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `18` | `18` | 37 | START | 37 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `20` | `20` | 37 | START | 37 | 77 |
| ✅ EXACT | `Action_RunBlock` | LG | `21` | `21` | 37 | START | 37 | 83 |
| ✅ EXACT | `Action_RunBlock` | LT | `4` | `4` | 37 | START | 37 | 52 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `16` | `16` | 56 | START | 56 | 67 |
| ✅ EXACT | `Action_BootAway` | QB | `16` | `16` | 68 | START | 68 | 116 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 118 | START | 118 | 130 |
| ✅ EXACT | `Action_SecureCatch` | TE2 | `19` | `19` | 170 | START | 170 | 186 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 30 | 7 | inferred_complete_timeline |
| `Action_None` | 31 | 55 | 25 | inferred_complete_timeline |
| `Action_FakeHandoff` | 56 | 67 | 12 | inferred_complete_timeline |
| `Action_BootAway` | 68 | 116 | 49 | inferred_complete_timeline |
| `Action_None` | 117 | 117 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 118 | 130 | 13 | inferred_complete_timeline |
| `Action_None` | 131 | 199 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 100 | 77 | inferred_complete_timeline |
| `Action_None` | 102 | 145 | 44 | inferred_complete_timeline |
| `Action_None` | 147 | 150 | 4 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 166 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 182 | 12 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 210 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 104 | 81 | inferred_complete_timeline |
| `Action_None` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 156 | 43 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 84 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_SecureCatch` | 170 | 186 | 17 | inferred_complete_timeline |
| `Action_None` | 187 | 199 | 13 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 37 | 52 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 37 | 83 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 30 | 7 | inferred_complete_timeline |
| `Action_None` | 31 | 36 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 37 | 115 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 37 | 77 | 41 | inferred_complete_timeline |
| `Action_RunBlock` | 85 | 113 | 29 | inferred_complete_timeline |
| `Action_RunBlock` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 141 | 210 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 37 | 67 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 69 | 80 | 12 | inferred_complete_timeline |
| `Action_RunBlock` | 98 | 115 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 176 | 153 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 186 | 4 | inferred_complete_timeline |
| `Action_None` | 188 | 196 | 9 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 115 | 92 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 136 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 52 | 29 | inferred_complete_timeline |
| `Action_None` | 68 | 89 | 22 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 113 | 12 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 139 | 8 | inferred_complete_timeline |
| `Action_None` | 144 | 210 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 100 | 77 | inferred_complete_timeline |
| `Action_None` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 118 | 203 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 193 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 119 | 96 | inferred_complete_timeline |
| `Action_None` | 121 | 199 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 141 | 118 | inferred_complete_timeline |
| `Action_None` | 144 | 172 | 29 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 193 | 170 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 51–210 | 160 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 80–188 | 99 | 4 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 89–210 | 122 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 93–136 | 43 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 136–210 | 75 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 146–210 | 65 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 170–210 | 41 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 73 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [24-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-119] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-199] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-156] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-115] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [37-52] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-193] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-89] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-113] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-139] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-100] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-193] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-172] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [37-115] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-176] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [37-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [69-80] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [98-115] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 187, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [187-199] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [37-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [85-113] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [122-123] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [135-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [141-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [37-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-138] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-119] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-136] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '28' has 1 frames without a visible bounding box.
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

</details>