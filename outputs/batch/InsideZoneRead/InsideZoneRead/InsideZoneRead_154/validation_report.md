# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_154`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_154/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '8' has invalid range: start=67, end=63. Clamping end to start.
> - Action 'Action_None' range [64-149] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-173] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [175-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-220] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-66] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-76] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-239] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-63] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-221] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-208] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-220] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [223-237] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-188] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-182] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-234] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-46] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-239] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-169] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-181] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-237] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-222] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '28' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_154'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.