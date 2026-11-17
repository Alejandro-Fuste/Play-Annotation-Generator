# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_80`
- **Input XML**: `outputs/batch/Power/Power/Power_80/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [19-96] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [82-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-192] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-132] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-138] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-156] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [82-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [94-103] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [82-97] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [104-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [126-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-95] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-159] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-21] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-198] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-209] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-208] for track '23' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.