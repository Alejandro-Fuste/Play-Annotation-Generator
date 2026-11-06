# Play-Annotation-Generator Annotation Review — OutsideZoneRead_129

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_129`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 121
- **Validation Errors:** 1
- **Overall Status:** FAILED

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
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Keep` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 23 | START | 23 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `14` | 23 | START | 23 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `17` | 23 | START | 23 | 32 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `20` | 23 | START | 23 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `7` | 23 | START | 23 | 33 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 29 | END | 29 | 29 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `16` | `15` | 36 | START | 36 | 43 |
| ✅ EXACT | `Action_Keep` | QB | `16` | `15` | 44 | START | 44 | 62 |
| ✅ EXACT | `Action_BallCarry` | QB | `16` | `15` | 63 | START | 63 | 164 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 125 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 29 | 1 | inferred_complete_timeline |
| `Action_None` | 30 | 35 | 6 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 36 | 43 | 8 | inferred_complete_timeline |
| `Action_Keep` | 44 | 62 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 63 | 164 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 21 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 61 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 239 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 180 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 233 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 119 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 201 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 210 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 239 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 33 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 96 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 33 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 93 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 125 | 16 | inferred_complete_timeline |
| `Action_None` | 126 | 144 | 19 | inferred_complete_timeline |
| `Action_None` | 146 | 161 | 16 | inferred_complete_timeline |
| `Action_None` | 163 | 210 | 48 | inferred_complete_timeline |
| `Action_None` | 212 | 239 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 34 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 42 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 32 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 68 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 85 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 57 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 128 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 69 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 94 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 142 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 239 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 112 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 150 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 163 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 188 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 160 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 174 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 224 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 229 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 187 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 235 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 68–71 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 84–228 | 127 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 85–239 | 152 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 88–239 | 140 | 5 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 92–211 | 73 | 6 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 127–239 | 91 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 141–239 | 89 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 184–239 | 51 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 185–221 | 37 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 205–238 | 32 | 2 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 208–222 | 14 | 2 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BallSnap' at frame 19 targets track ID '', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 94 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (LG) duration 103 frames exceeds threshold 90 frames [start=23, end=125].
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-233] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-33] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-160] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-174] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-188] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-224] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-42] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-93] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-161] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [63-164] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-239] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-142] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-187] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-235] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-57] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-21] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-87] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-145] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-228] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-201] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-239] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-91] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-98] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-142] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-212] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-141] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-219] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-219] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-188] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-221] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-231] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-238] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-215] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-222] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '33' has 1 frames without a visible bounding box.
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