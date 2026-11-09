# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_66`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_66/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 134: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-235] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-191] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-159] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-299] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-136] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [114-124] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-106] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-30] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-84] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-171] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-191] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-226] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-221] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-245] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-261] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-277] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-298] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.