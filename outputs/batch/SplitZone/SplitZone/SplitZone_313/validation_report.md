# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_313`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_313/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '15' has invalid range: start=127, end=122. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '17' has invalid range: start=194, end=172. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '18' has invalid range: start=199, end=172. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '19' has invalid range: start=204, end=172. Clamping end to start.
> - Action 'Action_None' range [120-271] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [133-162] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-172] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-208] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-161] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-268] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-252] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [138-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [166-219] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-222] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-291] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-143] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-297] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-161] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [167-307] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-236] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-277] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '23' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.