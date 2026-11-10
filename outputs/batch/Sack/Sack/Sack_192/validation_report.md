# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_192`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_192/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 44 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-204] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-228] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-237] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [209-239] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-215] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-236] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [190-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [195-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-216] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-214] for track '27' has 1 frames without a visible bounding box.
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