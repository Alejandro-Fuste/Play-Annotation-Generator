# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_1`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 25 |
| Ball Tracks | 4 |
| CSV events parsed | 22 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 509 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [348–361], lower_priority='Action_DownBlock' annotated_start=361, effective_Action_DownBlock_start=362.
> - Action 'Action_None' range [348-411] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-419] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [362-383] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-181] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-509] for track '28' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.