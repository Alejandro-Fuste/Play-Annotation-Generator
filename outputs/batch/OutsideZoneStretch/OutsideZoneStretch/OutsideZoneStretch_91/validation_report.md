# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_91`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 184: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 184: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_ZoneBlock' range [76-107] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-126] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-157] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-284] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-98] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-142] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-127] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-136] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [97-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-136] for track '14' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-329] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-215] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-293] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-320] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-200] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-207] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-215] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-274] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-325] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-300] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-327] for track '33' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.