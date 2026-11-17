# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_313`
- **Input XML**: `outputs/batch/Power/Power/Power_313/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [6-296] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-336] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-389] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-296] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-389] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-224] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-232] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-215] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-176] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [158-200] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-379] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [158-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-218] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-216] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-362] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-176] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-184] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-389] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-389] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-247] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-259] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-383] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-324] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-327] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-360] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-373] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.