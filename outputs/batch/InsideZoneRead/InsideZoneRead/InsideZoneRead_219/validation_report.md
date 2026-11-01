# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_219`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_219/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 34 |
| Ball Tracks | 1 |
| CSV events parsed | 21 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [83–100], lower_priority='Action_ZoneBlock' annotated_start=86, effective_Action_ZoneBlock_start=101.
> - Action 'Action_None' range [83-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-231] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-162] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-174] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-192] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-156] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-160] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [166-170] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-203] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [83-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [118-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [133-146] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [150-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-193] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-34] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-233] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-107] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [142-158] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-64] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-161] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-158] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-228] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-178] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-239] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-224] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-213] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-217] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-219] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '34' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.