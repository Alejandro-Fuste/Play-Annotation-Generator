# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_65`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_65/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-299] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-197] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-176] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-277] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-291] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-294] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-267] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-279] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-214] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-146] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-125] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-160] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-186] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-267] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-276] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [280-284] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-182] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-229] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-276] for track '24' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-294] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-237] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-277] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-273] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-281] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-290] for track '28' has 2 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.