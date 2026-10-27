# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_1`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 16 |
| Player Tracks | 16 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 50 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 298 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_PullBlock' at frame 51 targets track ID '[?]', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '2' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '1' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
> - Action 'Action_PreSnap' range [7-8] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [11-24] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [78-277] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-284] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-294] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [36-268] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [36-295] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-198] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-48] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-263] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [265-274] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-166] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-264] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-270] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-294] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [168-185] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-298] for track '15' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.