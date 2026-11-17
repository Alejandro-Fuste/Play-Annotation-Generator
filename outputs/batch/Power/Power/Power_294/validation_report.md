# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_294`
- **Input XML**: `outputs/batch/Power/Power/Power_294/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [5-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-298] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-246] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-140] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-118] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-294] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [101-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-160] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-241] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [101-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-110] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-142] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-27] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-192] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-198] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-223] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-168] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-221] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-223] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-276] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '23' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.