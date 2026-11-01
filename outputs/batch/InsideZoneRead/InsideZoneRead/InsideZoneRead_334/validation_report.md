# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_334`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_334/generated_base_cvat.xml`
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
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [58–69], lower_priority='Action_ZoneBlock' annotated_start=61, effective_Action_ZoneBlock_start=70.
> - Action 'Action_None' range [58-76] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-88] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-106] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-145] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [58-94] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-116] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-154] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-177] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-135] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-142] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-159] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-113] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-163] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-66] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-81] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-124] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-157] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [100-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-61] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-65] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-152] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-152] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-229] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.