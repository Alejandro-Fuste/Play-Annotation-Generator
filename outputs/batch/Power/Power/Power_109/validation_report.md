# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_109`
- **Input XML**: `outputs/batch/Power/Power/Power_109/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [6-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-137] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-190] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-206] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-77] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-99] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-115] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-50] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-69] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-168] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [39-43] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-135] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-99] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-103] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-192] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-37] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-124] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-138] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-160] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-201] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-167] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-169] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [171-176] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-71] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-209] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '26' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.