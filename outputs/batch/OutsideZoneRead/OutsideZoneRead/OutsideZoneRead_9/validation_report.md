# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_9`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 20: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-299] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-107] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-154] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-108] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-258] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-113] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-95] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-74] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-299] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-153] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-163] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-299] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-139] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-158] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-183] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-293] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '33' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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